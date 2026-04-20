# Theatre Square

> **Difficulty:** Easy | **Rating:** 1000 | **Tags:** `math`, `implementation`
> **Date Solved:** 2026-04-20

---

## 🔗 Problem Link

[1A — Theatre Square — Codeforces](https://codeforces.com/problemset/problem/1/A)

---

## 💡 Approach

### Intuition
Theatre Square has dimensions `n × m` meters. We need to pave it with square flagstones of size `a × a`. Flagstones cannot be broken, so if a dimension isn't perfectly divisible by `a`, we round up. The answer is the product of flagstones needed along each dimension.

### Optimized Logic

1. Calculate how many flagstones fit along the length: `ceil(n / a)`
2. Calculate how many flagstones fit along the width: `ceil(m / a)`
3. Multiply both values → total flagstones needed
4. **Key gotcha:** Use `long` (64-bit) because `n, m` can be up to 10⁹ and result can exceed 32-bit range

---

## 🧠 Concepts Used

- **Data Structures:** None (pure math)
- **Algorithms:** Ceiling division
- **Patterns:** Mathematical reasoning, integer overflow awareness

---

## ⏱ Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(1) |
| **Space** | O(1) |

---

## 🧪 Example

### Input
```
6 6 4
```

### Output
```
4
```

### Explanation
Theatre is 6×6. Each flagstone is 4×4. Along each dimension: `ceil(6/4) = 2`. Total = 2 × 2 = **4** flagstones.

---

## ✅ Solution Code

<details>
<summary>Java Solution ☕</summary>

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import static java.lang.Math.ceil;

/**
 * See <a href="http://codeforces.com/problemset/problem/1/A">Theatre Square</a>
 */
public class CF001ATheatreSquare {

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        String[] p = in.readLine().split("\\s");
        long n = Long.parseLong(p[0]);
        long m = Long.parseLong(p[1]);
        double a = Double.parseDouble(p[2]);
        long flagstones = (long) (ceil(n / a) * ceil(m / a));
        out.print(flagstones);
        out.close();
    }
}
```

</details>

<details>
<summary>Python Solution 🐍</summary>

```python
import math

def solve():
    n, m, a = map(int, input().split())
    # Ceiling division: (x + y - 1) // y avoids floating point issues
    rows = (n + a - 1) // a
    cols = (m + a - 1) // a
    print(rows * cols)

solve()
```

</details>

<details>
<summary>C++ Solution</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, m, a;
    cin >> n >> m >> a;
    cout << ((n + a - 1) / a) * ((m + a - 1) / a) << endl;
    return 0;
}
```

</details>

---

## 📌 Key Takeaways

- Ceiling division is a fundamental technique: `ceil(x/y)` = `(x + y - 1) / y` (integer-only, no float)
- Always watch for **integer overflow** when multiplying large numbers — use `long` / `long long`
- This is CF Problem #1 — classic starter problem for Codeforces

---

## 🔗 Related Problems

- [1B — Spreadsheets](https://codeforces.com/problemset/problem/1/B)
- [4A — Watermelon](https://codeforces.com/problemset/problem/4/A)
