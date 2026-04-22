# Domino Piling

> **Difficulty:** Easy | **Rating:** 800 | **Tags:** `math`, `greedy`, `implementation`
> **Date Solved:** 2026-04-22

---

## Problem Link

[50A - Domino Piling - Codeforces](https://codeforces.com/problemset/problem/50/A)

---

## Approach

### Intuition
A domino covers exactly 2 cells. For an `M x N` board, the total number of cells is `M * N`. To place the maximum number of dominoes without overlapping or going outside the board, we only need to count how many pairs of cells can be formed.

### Optimized Logic

1. Read the board dimensions `M` and `N`.
2. Calculate the board area: `M * N`.
3. Each domino covers 2 squares, so the answer is `(M * N) / 2`.
4. Integer division automatically discards one leftover square when the area is odd.

---

## Concepts Used

- **Data Structures:** None (pure math)
- **Algorithms:** Arithmetic counting
- **Patterns:** Greedy counting, mathematical reasoning

---

## Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(1) |
| **Space** | O(1) |

---

## Example

### Input
```
2 4
```

### Output
```
4
```

### Explanation
The board has `2 x 4 = 8` cells. Each domino covers 2 cells, so the maximum number of dominoes is `8 / 2 = 4`.

---

## Solution Code

<details>
<summary>Java Solution</summary>

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class CF050ADominoPiling {

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        String[] p = in.readLine().split("\\s");
        int M = Integer.parseInt(p[0]);
        int N = Integer.parseInt(p[1]);
        int area = M * N;
        out.println(area / 2);
        out.close();
    }
}
```

</details>

<details>
<summary>Go Solution</summary>

```go
package main

import "fmt"

func main() {
    var m, n int
    fmt.Scan(&m, &n)
    fmt.Println((m * n) / 2)
}
```

</details>

<details>
<summary>Python Solution</summary>

```python
def solve():
    m, n = map(int, input().split())
    print((m * n) // 2)

solve()
```

</details>

---

## Key Takeaways

- When each item covers 2 cells, the maximum count is simply `area / 2`.
- Integer division handles odd board areas by leaving one square unused.
- Some Codeforces problems are direct mathematical observations; avoid overcomplicating them.

---

## Related Problems

- [1A - Theatre Square](https://codeforces.com/problemset/problem/1/A)
- [4A - Watermelon](https://codeforces.com/problemset/problem/4/A)
