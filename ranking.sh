#!/bin/bash
set -euo pipefail

OWNER="ianzepp"
SKIP="archived-projects personal ianzepp.dev dotfiles homebrew-tap 0-prework-assignment"

echo "Fetching repo data from GitHub API..."
repo_json=$(gh repo list "$OWNER" --limit 200 --json name,description,isPrivate,isFork)

# Count commits via API (no cloning needed)
declare -A counts
declare -A descs
declare -A visibility

for name in $(echo "$repo_json" | jq -r '.[].name' | sort); do
  echo "$SKIP" | grep -qw "$name" && continue

  is_fork=$(echo "$repo_json" | jq -r --arg n "$name" '.[] | select(.name == $n) | .isFork')
  [ "$is_fork" = "true" ] && continue

  # Get commit count from the default branch via API
  count=$(gh api "repos/$OWNER/$name/commits?per_page=1" -i 2>/dev/null \
    | grep -i '^link:' \
    | sed 's/.*page=\([0-9]*\)>.*/\1/' || echo "1")
  [ -z "$count" ] && count=1

  desc=$(echo "$repo_json" | jq -r --arg n "$name" '.[] | select(.name == $n) | .description // ""')
  is_private=$(echo "$repo_json" | jq -r --arg n "$name" '.[] | select(.name == $n) | .isPrivate')

  counts[$name]=$count
  descs[$name]=${desc:-$name}
  visibility[$name]=$( [ "$is_private" = "true" ] && echo "private" || echo "public" )
  echo "  $name: $count commits"
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
  label=$( [ "${visibility[$name]}" = "private" ] && echo "[private] " || echo "" )
  entry="${label}$name ($count commits) - ${descs[$name]}"
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
