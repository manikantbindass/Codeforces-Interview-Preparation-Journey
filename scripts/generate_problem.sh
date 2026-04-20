#!/bin/bash
# ============================================
# generate_problem.sh
# Auto-create a new problem file from template
# ============================================
# Usage: bash scripts/generate_problem.sh "Problem Name" easy "math,arrays" 800

set -e

# Arguments
PROBLEM_NAME="${1:?Error: Problem name required}"
DIFFICULTY="${2:?Error: Difficulty required (easy/medium/hard)}"
TAGS="${3:-general}"
RATING="${4:-0}"
DATE=$(date +%Y-%m-%d)

# Validate difficulty
if [[ "$DIFFICULTY" != "easy" && "$DIFFICULTY" != "medium" && "$DIFFICULTY" != "hard" ]]; then
    echo "❌ Error: Difficulty must be 'easy', 'medium', or 'hard'"
    exit 1
fi

# Get script directory (repo root)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

# Count existing problems in difficulty folder
PROBLEM_DIR="$REPO_ROOT/problems/$DIFFICULTY"
mkdir -p "$PROBLEM_DIR"
COUNT=$(ls -1 "$PROBLEM_DIR"/*.md 2>/dev/null | wc -l)
NEXT_NUM=$(printf "%03d" $((COUNT + 1)))

# Generate filename (lowercase, underscores)
FILENAME=$(echo "$PROBLEM_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '_' | tr -cd 'a-z0-9_')
FILEPATH="$PROBLEM_DIR/${NEXT_NUM}_${FILENAME}.md"

# Format tags for display
TAG_DISPLAY=$(echo "$TAGS" | tr ',' ', ')
TAG_BACKTICK=$(echo "$TAGS" | sed 's/,/`, `/g' | sed 's/^/`/' | sed 's/$/ `/' | sed 's/ $//')

# Capitalize difficulty
DIFF_UPPER="$(tr '[:lower:]' '[:upper:]' <<< ${DIFFICULTY:0:1})${DIFFICULTY:1}"

# Generate problem file
cat > "$FILEPATH" << EOF
# $PROBLEM_NAME

> **Difficulty:** $DIFF_UPPER | **Rating:** $RATING | **Tags:** $TAG_BACKTICK
> **Date Solved:** $DATE

---

## 🔗 Problem Link

[${PROBLEM_NAME} — Codeforces](https://codeforces.com/problemset/problem/XXX/X)

---

## 💡 Approach

### Intuition
<!-- Explain the core idea in simple terms -->

### Optimized Logic
<!-- Step-by-step breakdown -->

1. Step 1
2. Step 2
3. Step 3

---

## 🧠 Concepts Used

- **Data Structures:** 
- **Algorithms:** 
- **Patterns:** 

---

## ⏱ Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(?) |
| **Space** | O(?) |

---

## 🧪 Example

### Input
\`\`\`
<input>
\`\`\`

### Output
\`\`\`
<output>
\`\`\`

### Explanation
<!-- Walk through the example -->

---

## ✅ Solution Code

<details>
<summary>C++ Solution</summary>

\`\`\`cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    // Solution here
    
    return 0;
}
\`\`\`

</details>

<details>
<summary>Python Solution</summary>

\`\`\`python
# Solution here
\`\`\`

</details>

<details>
<summary>Java Solution</summary>

\`\`\`java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Solution here
    }
}
\`\`\`

</details>

---

## 📌 Key Takeaways

- 
- 
- 

---

## 🔗 Related Problems

- 
EOF

echo "✅ Created: $FILEPATH"
echo "📝 Problem: $PROBLEM_NAME"
echo "🎯 Difficulty: $DIFF_UPPER"
echo "🏷️  Tags: $TAG_DISPLAY"
echo "⭐ Rating: $RATING"
echo ""
echo "Don't forget to update the README stats: python scripts/update_readme.py"
