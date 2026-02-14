#!/bin/bash
set -euo pipefail

OWNER="ianzepp"
BASE_DIR="${1:-$(pwd)/repos}"
SKIP="archived-projects personal ianzepp.dev dotfiles homebrew-tap 0-prework-assignment"

# Clone or update all repos
echo "Fetching repo list from GitHub..."
repos=$(gh repo list "$OWNER" --limit 200 --json name --jq '.[].name' | sort)

mkdir -p "$BASE_DIR"

for repo in $repos; do
  if echo "$SKIP" | grep -qw "$repo"; then
    continue
  fi
  if [ -d "$BASE_DIR/$repo/.git" ]; then
    git -C "$BASE_DIR/$repo" fetch --quiet 2>/dev/null || true
  else
    echo "Cloning $repo..."
    gh repo clone "$OWNER/$repo" "$BASE_DIR/$repo" -- --quiet 2>/dev/null || true
  fi
done

# Count commits and collect descriptions
declare -A counts
declare -A descs

desc_json=$(gh repo list "$OWNER" --limit 200 --json name,description)

for dir in "$BASE_DIR"/*/; do
  [ -d "$dir/.git" ] || continue
  name=$(basename "$dir")
  echo "$SKIP" | grep -qw "$name" && continue
  count=$(git -C "$dir" rev-list --count HEAD 2>/dev/null || echo 0)
  desc=$(echo "$desc_json" | jq -r --arg n "$name" '.[] | select(.name == $n) | .description // ""')
  counts[$name]=$count
  descs[$name]=${desc:-$name}
done

# Sort by commit count descending
sorted=$(for name in "${!counts[@]}"; do
  echo "${counts[$name]} $name"
done | sort -rn)

# Split into tiers
featured=()
previous=()
other=()
rank=0

while read -r count name; do
  [ "$count" -lt 5 ] && continue
  rank=$((rank + 1))
  entry="$name ($count commits) - ${descs[$name]}"
  if [ "$rank" -le 5 ]; then
    featured+=("$entry")
  elif [ "$count" -gt 20 ]; then
    previous+=("$entry")
  else
    other+=("$entry")
  fi
done <<< "$sorted"

# Report
echo ""
echo "=== Featured Work (top 5) ==="
for e in "${featured[@]}"; do echo "  $e"; done

echo ""
echo "=== Previous Projects (>20 commits) ==="
if [ ${#previous[@]} -gt 0 ]; then
  for e in "${previous[@]}"; do echo "  $e"; done
else
  echo "  (none)"
fi

echo ""
echo "=== Other (5+ commits) ==="
if [ ${#other[@]} -gt 0 ]; then
  for e in "${other[@]}"; do echo "  $e"; done
else
  echo "  (none)"
fi

# Summary
total=${#counts[@]}
included=$((${#featured[@]} + ${#previous[@]} + ${#other[@]}))
echo ""
echo "Total repos: $total | Listed: $included | Skipped (<5 commits): $((total - included))"
