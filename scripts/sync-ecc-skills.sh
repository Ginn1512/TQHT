#!/usr/bin/env bash
# Đồng bộ skills từ ECC (https://github.com/affaan-m/ECC) vào .claude/skills/.
#
# Cách dùng:
#   scripts/sync-ecc-skills.sh            # lấy bản mới nhất trên nhánh main
#   scripts/sync-ecc-skills.sh <ref>      # lấy theo tag/nhánh/commit, ví dụ v2.2.2
#
# Chỉ thay các skill có tên trong third_party/ecc/skills.txt (lần đồng bộ trước)
# hoặc có trong ECC; skill bạn tự viết trong .claude/skills/ không bị động tới.
#
# Nếu có third_party/ecc/keep.txt thì chỉ chép các skill liệt kê trong đó
# (mỗi dòng một tên, dòng bắt đầu bằng # là ghi chú). Xoá keep.txt để lấy lại đủ bộ.
set -euo pipefail

REPO_URL="https://github.com/affaan-m/ECC.git"
REF="${1:-main}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$ROOT/.claude/skills"
META_DIR="$ROOT/third_party/ecc"
MANIFEST="$META_DIR/skills.txt"
KEEP="$META_DIR/keep.txt"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

git clone --quiet --depth 1 --branch "$REF" "$REPO_URL" "$TMP/ECC" 2>/dev/null \
  || { git clone --quiet "$REPO_URL" "$TMP/ECC" && git -C "$TMP/ECC" checkout --quiet "$REF"; }

mkdir -p "$SKILLS_DIR" "$META_DIR"

# Xoá các skill ECC của lần đồng bộ trước (kể cả skill upstream đã gỡ bỏ).
if [[ -f "$MANIFEST" ]]; then
  while IFS= read -r name; do
    [[ -n "$name" ]] && rm -rf "${SKILLS_DIR:?}/$name"
  done < "$MANIFEST"
fi

if [[ -f "$KEEP" ]]; then
  names=()
  while IFS= read -r line; do
    name="${line%%#*}"
    name="${name//[[:space:]]/}"
    [[ -z "$name" ]] && continue
    if [[ ! "$name" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
      echo "Bỏ qua tên không hợp lệ trong keep.txt: $line" >&2
      continue
    fi
    names+=("$name")
  done < "$KEEP"
else
  names=()
  for dir in "$TMP/ECC/skills"/*/; do
    names+=("$(basename "$dir")")
  done
fi

: > "$MANIFEST.new"
for name in "${names[@]}"; do
  dir="$TMP/ECC/skills/$name"
  if [[ ! -f "$dir/SKILL.md" ]]; then
    echo "Cảnh báo: ECC không có skill '$name'" >&2
    continue
  fi
  cp -R "$dir" "$SKILLS_DIR/$name"
  echo "$name" >> "$MANIFEST.new"
done
mv "$MANIFEST.new" "$MANIFEST"

cp "$TMP/ECC/LICENSE" "$META_DIR/LICENSE"
{
  echo "repo: $REPO_URL"
  echo "ref: $REF"
  echo "commit: $(git -C "$TMP/ECC" rev-parse HEAD)"
  echo "version: $(cat "$TMP/ECC/VERSION" 2>/dev/null || echo unknown)"
} > "$META_DIR/SOURCE"

echo "Đã đồng bộ $(wc -l < "$MANIFEST") skills từ ECC ($(git -C "$TMP/ECC" rev-parse --short HEAD))."
