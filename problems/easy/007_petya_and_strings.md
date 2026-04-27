# Petya and Strings

> **Difficulty:** Easy | **Rating:** 800 | **Tags:** `implementation`, `strings`
> **Date Solved:** 2026-04-27

---

## Problem Link

[112A - Petya and Strings - Codeforces](https://codeforces.com/problemset/problem/112/A)

---

## Approach

### Intuition
We need to compare two strings lexicographically, but uppercase and lowercase letters should be treated as equal. That means the comparison must ignore case entirely.

### Optimized Logic

1. Read the two input strings.
2. Compare them using Java's `compareToIgnoreCase`.
3. If the result is positive, print `1`.
4. If the result is negative, print `-1`.
5. Otherwise, print `0`.

### Why This Works
`compareToIgnoreCase` performs lexicographical comparison while treating corresponding uppercase and lowercase letters as equal. The sign of its return value matches the exact output the problem asks for.

---

## Concepts Used

- **Data Structures:** Strings
- **Algorithms:** Lexicographical comparison
- **Patterns:** Case-insensitive comparison, implementation

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
abs
Abz
```

### Output
```text
-1
```

### Explanation
Ignoring case gives `abs` and `abz`. Since `abs` comes before `abz` lexicographically, the answer is `-1`.

### Input
```text
aaaa
aaaA
```

### Output
```text
0
```

### Explanation
Both strings are identical when case is ignored, so the comparison result is `0`.

---

## Solution Code

<details>
<summary>Java Solution</summary>

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class CF112APetyaAndStrings {

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        String a = in.readLine();
        String b = in.readLine();
        int difference = a.compareToIgnoreCase(b);
        if (difference > 0) {
            out.print(1);
        } else if (difference < 0) {
            out.print(-1);
        } else {
            out.print(0);
        }
        out.close();
    }
}
```

</details>

---

## Key Takeaways

- Built-in string comparison methods can solve many implementation problems cleanly.
- When a problem says case does not matter, compare normalized strings or use a case-insensitive API.
- The sign of a comparison result is often all you need instead of manual character-by-character logic.

---

## Related Problems

- [58A - Chat room](https://codeforces.com/problemset/problem/58/A)
- [118A - String Task](https://codeforces.com/problemset/problem/118/A)
- [71A - Way Too Long Words](https://codeforces.com/problemset/problem/71/A)
