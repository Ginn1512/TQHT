"""Mở trang wiki nguồn để kiểm khẳng định (dùng cho /kaku-canon-ledger).

    python -m tools.wiki https://frieren.fandom.com/wiki/Zoltraak
    python -m tools.wiki https://frieren.fandom.com/wiki/Zoltraak --grep Qual "80 years" --context 1
    python -m tools.wiki https://en.wikipedia.org/wiki/Frieren --grep Zoltraak

Trang fandom bị Cloudflare chặn khi mở thẳng từ máy chủ (403 "challenge"), nhưng API
MediaWiki của chính wiki đó vẫn trả toàn văn trang. Wikipedia đọc qua `action=raw`.
Kết quả là nội dung thật của trang, không phải đoạn trích tìm kiếm, nên được tính là
"đã mở trang". Khi `canon resolve`, ghi link trang người đọc (…/wiki/<Tên>), không ghi
link API.

--grep chỉ in các dòng có từ khóa (không phân biệt hoa thường) và vài dòng quanh đó,
để khỏi đọc cả trang dài. Không có --grep thì in cả trang (cắt ở --max ký tự).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

USER_AGENT = "TQHT-factcheck/1.0 (https://github.com/Ginn1512/TQHT)"


def page_title(url: str) -> tuple[str, str]:
    """(host, tên trang) từ link dạng https://<host>/wiki/<Tên>."""
    parts = urllib.parse.urlsplit(url)
    if not parts.path.startswith("/wiki/"):
        raise ValueError(f"không phải link trang wiki (cần /wiki/<Tên>): {url}")
    title = urllib.parse.unquote(parts.path[len("/wiki/") :]).split("#")[0]
    return parts.netloc, title


def api_url(url: str) -> str:
    """Link lấy toàn văn (wikitext) của trang."""
    host, title = page_title(url)
    q = urllib.parse.quote(title, safe="")
    if host.endswith(".fandom.com"):
        return f"https://{host}/api.php?action=parse&page={q}&prop=wikitext&format=json&formatversion=2&redirects=1"
    if host.endswith(".wikipedia.org"):
        return f"https://{host}/w/index.php?title={q}&action=raw"
    raise ValueError(f"chưa hỗ trợ {host}: chỉ *.fandom.com và *.wikipedia.org")


def _get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Không mở được {url}: HTTP {e.code}. Giữ dòng ở mức chưa kiểm.") from e
    except (urllib.error.URLError, TimeoutError) as e:
        raise SystemExit(f"Không mở được {url}: {e}. Giữ dòng ở mức chưa kiểm.") from e


def fetch(url: str) -> str:
    """Wikitext của trang; đi theo trang chuyển hướng một lần."""
    body = _get(api_url(url))
    if ".fandom.com" in url:
        data = json.loads(body)
        if "error" in data:
            raise SystemExit(f"Wiki báo lỗi cho {url}: {data['error'].get('info', data['error'])}")
        return data["parse"]["wikitext"]
    m = re.match(r"#REDIRECT\s*\[\[([^\]|#]+)", body, re.I)
    if m:
        host, _ = page_title(url)
        return _get(api_url(f"https://{host}/wiki/{m.group(1).replace(' ', '_')}"))
    return body


def clean(wikitext: str) -> str:
    """Bỏ chú thích <ref>, gọn link [[a|b]] thành b, bỏ '' và ''' ."""
    text = re.sub(r"<ref[^>/]*/>", "", wikitext)
    text = re.sub(r"<ref[^>]*>.*?</ref>", "", text, flags=re.S)
    text = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", text)
    text = re.sub(r"'{2,}", "", text)
    return re.sub(r"\n{3,}", "\n\n", text)


def grep(text: str, words: list[str], context: int = 1) -> str:
    """Các dòng có một trong các từ khóa, kèm `context` dòng trước và sau; nhóm cách nhau bằng ---."""
    lines = text.splitlines()
    pattern = re.compile("|".join(re.escape(w) for w in words), re.I)
    keep: set[int] = set()
    for i, line in enumerate(lines):
        if pattern.search(line):
            keep.update(range(max(0, i - context), min(len(lines), i + context + 1)))
    out, last = [], -2
    for i in sorted(keep):
        if i != last + 1 and out:
            out.append("---")
        out.append(lines[i])
        last = i
    return "\n".join(out)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("url", help="link trang, dạng https://<wiki>.fandom.com/wiki/<Tên> hoặc https://en.wikipedia.org/wiki/<Tên>")
    p.add_argument("--grep", nargs="+", metavar="TỪ", help="chỉ in dòng có các từ này")
    p.add_argument("--context", type=int, default=1, help="số dòng in thêm quanh mỗi dòng khớp (mặc định 1)")
    p.add_argument("--max", type=int, default=20000, help="số ký tự tối đa khi in cả trang (mặc định 20000)")
    args = p.parse_args()
    try:
        text = clean(fetch(args.url))
    except ValueError as e:
        raise SystemExit(str(e)) from e
    if args.grep:
        found = grep(text, args.grep, args.context)
        print(found or f"Không có dòng nào chứa: {', '.join(args.grep)}")
        return
    print(text[: args.max])
    if len(text) > args.max:
        print(f"\n[… cắt ở {args.max}/{len(text)} ký tự; dùng --grep để tìm đúng đoạn]", file=sys.stderr)


if __name__ == "__main__":
    main()
