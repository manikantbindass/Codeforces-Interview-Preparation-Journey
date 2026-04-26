# Young Physicist

> **Difficulty:** Easy | **Rating:** 1000 | **Tags:** `implementation`, `math`
> **Date Solved:** 2026-04-26

---

## Problem Link

[69A - Young Physicist - Codeforces](https://codeforces.com/problemset/problem/69/A)

---

## Approach

### Intuition
Each force vector contributes to the final force on the body. The body is in equilibrium only if the total force along the `x`, `y`, and `z` axes is zero, so we just sum each coordinate across all vectors.

### Optimized Logic

1. Read `n`, the number of force vectors.
2. Keep running sums for the `x`, `y`, and `z` coordinates.
3. Add each vector's coordinates to those sums.
4. If all three sums are zero at the end, print `YES`; otherwise print `NO`.

### Why This Works
The vector sum of multiple forces is found by adding their components independently. Equilibrium means the resultant vector is `(0, 0, 0)`, so checking the three final coordinate sums is both necessary and sufficient.

---

## Concepts Used

- **Data Structures:** Integer variables
- **Algorithms:** Linear scan
- **Patterns:** Coordinate aggregation, implementation

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
3
4 1 7
-2 4 -1
1 -5 -3
```

### Output
```text
NO
```

### Explanation
The total force becomes `(3, 0, 3)`, which is not the zero vector, so the body is not in equilibrium.

### Input
```text
3
3 -1 7
-5 2 -4
2 -1 -3
```

### Output
```text
YES
```

### Explanation
The coordinate sums are `0`, `0`, and `0`, so the net force is zero and the body stays in equilibrium.

---

## Solution Code

<details>
<summary>Java Solution</summary>

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class CF69AYoungPhysicist {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();
        int n = fs.nextInt();

        int x = 0;
        int y = 0;
        int z = 0;

        for (int i = 0; i < n; i++) {
            x += fs.nextInt();
            y += fs.nextInt();
            z += fs.nextInt();
        }

        System.out.println(x == 0 && y == 0 && z == 0 ? "YES" : "NO");
    }

    static class FastScanner {
        private final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        private StringTokenizer st;

        int nextInt() throws IOException {
            while (st == null || !st.hasMoreElements()) {
                st = new StringTokenizer(br.readLine());
            }
            return Integer.parseInt(st.nextToken());
        }
    }
}
```

</details>

<details>
<summary>Python Solution</summary>

```python
import sys


def main():
    input = sys.stdin.read
    data = list(map(int, input().split()))

    n = data[0]
    x = y = z = 0
    idx = 1

    for _ in range(n):
        x += data[idx]
        y += data[idx + 1]
        z += data[idx + 2]
        idx += 3

    if x == 0 and y == 0 and z == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
```

</details>

<details>
<summary>Go Solution</summary>

```go
package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	x, y, z := 0, 0, 0
	for i := 0; i < n; i++ {
		var a, b, c int
		fmt.Scan(&a, &b, &c)
		x += a
		y += b
		z += c
	}

	if x == 0 && y == 0 && z == 0 {
		fmt.Println("YES")
	} else {
		fmt.Println("NO")
	}
}
```

</details>

---

## Key Takeaways

- Many 3D vector problems reduce to summing each coordinate independently.
- Equilibrium questions often become a direct zero-sum check.
- A single pass with constant extra space is enough for this problem.

---

## Related Problems

- [1A - Theatre Square](https://codeforces.com/problemset/problem/1/A)
- [50A - Domino Piling](https://codeforces.com/problemset/problem/50/A)
- [486A - Calculating Function](https://codeforces.com/problemset/problem/486/A)
