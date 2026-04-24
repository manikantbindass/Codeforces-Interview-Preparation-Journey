# Chat room

> **Difficulty:** Easy | **Rating:** 1000 | **Tags:** `greedy`, `strings`
> **Date Solved:** 2026-04-24

---

## Problem Link

[58A - Chat room - Codeforces](https://codeforces.com/problemset/problem/58/A)

---

## Approach

### Intuition
We need to check whether the word `hello` appears as a subsequence inside the given string. Characters do not need to be adjacent, but they must appear in the same order.

### Optimized Logic

1. Read the input string.
2. Search for the letters `h`, `e`, `l`, `l`, and `o` in order.
3. If all letters appear in the required order, print `YES`.
4. Otherwise, print `NO`.

### Why This Works
Deleting extra characters from the input is exactly the same as checking whether `hello` is a subsequence. The regular expression `.*h.*e.*l.*l.*o.*` verifies that the required letters appear in order with any number of characters between them.

---

## Concepts Used

- **Data Structures:** String
- **Algorithms:** Subsequence matching
- **Patterns:** Greedy scan, string matching

---

## Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n) |
| **Space** | O(1) |

---

## Example

### Input
```text
ahhellllloou
```

### Output
```text
YES
```

### Explanation
The letters `h`, `e`, `l`, `l`, and `o` appear in order, so the word `hello` can be formed.

### Input
```text
hlelo
```

### Output
```text
NO
```

### Explanation
The letters do not appear in the exact order needed to form `hello`.

---

## Solution Code

<details>
<summary>Python Solution</summary>

```python
import sys
import re


def main():
    s = sys.stdin.readline().strip()
    if re.match(r'.*h.*e.*l.*l.*o.*', s):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
```

</details>

---

## Key Takeaways

- Subsequence problems care about order, not adjacency.
- A greedy scan or a simple regular expression can solve this efficiently.
- Always map the wording "delete some characters" to a possible subsequence check.

---

## Related Problems

- [4A - Watermelon](https://codeforces.com/problemset/problem/4/A)
- [118A - String Task](https://codeforces.com/problemset/problem/118/A)
- [96A - Football](https://codeforces.com/problemset/problem/96/A)
