#!/usr/bin/env bash
# Đồng bộ skills từ ECC (https://github.com/affaan-m/ECC) vào .claude/skills/.
#
# Cách dùng:
#   scripts/sync-ecc-skills.sh            # lấy bản mới nhất trên nhánh main
#   scripts/sync-ecc-skills.sh <ref>      # lấy theo tag/nhánh/commit, ví dụ v2.2.2
#
# Chỉ thay các skill có tên trong third_party/ecc/skills.txt (lần đồng bộ trước)
# hoặc có trong ECC; skill bạn tự viết trong .claude/skills/ không bị động tới.
set -euo pipefail

REPO_URL="https://github.com/affaan-m/ECC.git"
REF="${1:-main}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="$ROOT/.claude/skills"
META_DIR="$ROOT/third_party/ecc"
MANIFEST="$META_DIR/skills.txt"

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

: > "$MANIFEST.new"
for dir in "$TMP/ECC/skills"/*/; do
  name="$(basename "$dir")"
  [[ -f "$dir/SKILL.md" ]] || continue
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
