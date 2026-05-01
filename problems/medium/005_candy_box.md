# Candy Box (easy version)

> **Difficulty:** Medium | **Rating:** 1400 | **Tags:** `greedy`, `sortings`
> **Date Solved:** 2026-05-01

---

## Problem Link

[1183D - Candy Box (easy version) - Codeforces](https://codeforces.com/problemset/problem/1183/D)

---

## Approach

### Intuition
We only care about how many candies each type appears, not the actual type values. After collecting those frequencies, we want to choose the largest possible set of counts such that every chosen count is positive and strictly smaller than the previous one.

### Optimized Logic

1. For each test case, count the frequency of every candy type.
2. Put all frequencies into a list and sort it in descending order.
3. Walk from left to right and cap each frequency so it becomes at most `previous - 1`.
4. If a capped frequency becomes negative or zero, it contributes nothing more.
5. Sum all remaining positive frequencies.

### Why This Works
Sorting puts the largest frequencies first, so greedily taking as many as possible from each one leaves the best chance to keep later frequencies distinct and positive. Reducing each next value to at most `previous - 1` guarantees all chosen frequencies are strictly decreasing while preserving the maximum total sum.

---

## Concepts Used

- **Data Structures:** Hash map, array/list
- **Algorithms:** Frequency counting, sorting, greedy adjustment
- **Patterns:** Greedy, sorting

---

## Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(n log n) per test case |
| **Space** | O(n) |

---

## Example

### Input
```text
3
8
1 4 8 4 5 6 3 8
16
2 1 3 3 4 3 4 4 1 3 2 2 2 4 1 1
9
2 2 4 4 4 7 7 7 7
```

### Output
```text
3
10
9
```

### Explanation
For each test case, we count how many times each candy type appears, sort those counts, and then make them strictly decreasing. The resulting positive frequencies give the largest valid gift size.

---

## Solution Code

<details>
<summary>Java Solution</summary>

```java
import java.io.BufferedInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class CF1183DCandyBox {

    public static void main(String[] args) throws Exception {
        FastScanner sc = new FastScanner();
        StringBuilder out = new StringBuilder();

        int t = sc.nextInt();

        while (t-- > 0) {
            int n = sc.nextInt();

            HashMap<Integer, Integer> map = new HashMap<>();

            for (int i = 0; i < n; i++) {
                int x = sc.nextInt();
                map.put(x, map.getOrDefault(x, 0) + 1);
            }

            ArrayList<Integer> dp = new ArrayList<>(map.values());
            Collections.sort(dp, Collections.reverseOrder());

            long ans = 0;

            for (int i = 1; i < dp.size(); i++) {
                dp.set(i, Math.min(dp.get(i), dp.get(i - 1) - 1));
            }

            for (int x : dp) {
                if (x > 0) {
                    ans += x;
                }
            }

            out.append(ans).append('\n');
        }

        System.out.print(out);
    }

    static class FastScanner {
        private final BufferedInputStream in = new BufferedInputStream(System.in);
        private final byte[] buffer = new byte[1 << 16];
        private int ptr = 0;
        private int len = 0;

        private int read() throws IOException {
            if (ptr >= len) {
                len = in.read(buffer);
                ptr = 0;
                if (len <= 0) {
                    return -1;
                }
            }
            return buffer[ptr++];
        }

        int nextInt() throws IOException {
            int c;
            do {
                c = read();
            } while (c <= ' ' && c != -1);

            int sign = 1;
            if (c == '-') {
                sign = -1;
                c = read();
            }

            int value = 0;
            while (c > ' ') {
                value = value * 10 + (c - '0');
                c = read();
            }
            return value * sign;
        }
    }
}
```

</details>

<details>
<summary>Python Solution</summary>

```python
from collections import Counter
import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    index = 1
    answers = []

    for _ in range(t):
        n = data[index]
        index += 1
        freq = Counter(data[index:index + n])
        index += n

        counts = sorted(freq.values(), reverse=True)

        for i in range(1, len(counts)):
            counts[i] = min(counts[i], counts[i - 1] - 1)

        total = 0
        for value in counts:
            if value > 0:
                total += value

        answers.append(str(total))

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()
```

</details>

<details>
<summary>Go Solution</summary>

```go
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	in := bufio.NewReaderSize(os.Stdin, 1<<20)
	out := bufio.NewWriterSize(os.Stdout, 1<<20)
	defer out.Flush()

	var t int
	fmt.Fscan(in, &t)

	for ; t > 0; t-- {
		var n int
		fmt.Fscan(in, &n)

		freq := make(map[int]int)
		for i := 0; i < n; i++ {
			var x int
			fmt.Fscan(in, &x)
			freq[x]++
		}

		counts := make([]int, 0, len(freq))
		for _, value := range freq {
			counts = append(counts, value)
		}

		sort.Sort(sort.Reverse(sort.IntSlice(counts)))

		for i := 1; i < len(counts); i++ {
			if counts[i] > counts[i-1]-1 {
				counts[i] = counts[i-1] - 1
			}
		}

		var ans int64
		for _, value := range counts {
			if value > 0 {
				ans += int64(value)
			}
		}

		fmt.Fprintln(out, ans)
	}
}
```

</details>

---

## Key Takeaways

- Once the original values stop mattering, frequency compression often reveals the real problem.
- Sorting frequencies first makes the greedy choice natural and optimal here.
- Enforcing a strictly decreasing sequence is a common trick in counting and allocation problems.

---

## Related Problems

- [1183G - Candy Box (hard version)](https://codeforces.com/problemset/problem/1183/G)
- [1174B - Ehab Is an Odd Person](https://codeforces.com/problemset/problem/1174/B)
- [1605C - Dominant Character](https://codeforces.com/problemset/problem/1605/C)
