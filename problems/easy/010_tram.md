# Tram

> **Difficulty:** Easy | **Rating:** 800 | **Tags:** `implementation`
> **Date Solved:** 2026-04-30

---

## Problem Link

[116A - Tram - Codeforces](https://codeforces.com/problemset/problem/116/A)

---

## Approach

### Intuition
The tram starts empty. At each stop, some passengers leave and some enter, so we only need to track how many passengers are currently inside and remember the highest value reached at any point.

### Optimized Logic

1. Read the number of stops `n`.
2. Maintain `passengers` for the current number inside the tram.
3. For every stop, subtract the exiting passengers and add the entering passengers.
4. Update `capacity` with the maximum value of `passengers` seen so far.
5. Print `capacity` after processing all stops.

### Why This Works
The required answer is the minimum tram capacity that never gets exceeded. That is exactly the maximum number of passengers present after processing any stop, so a single linear scan is enough.

---

## Concepts Used

- **Data Structures:** Integer variables
- **Algorithms:** Linear scan, running maximum
- **Patterns:** Implementation, simulation

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
4
0 3
2 5
4 2
4 0
```

### Output
```text
6
```

### Explanation
The passenger count after each stop becomes `3`, `6`, `4`, and `0`. The largest value reached is `6`, so the tram must have capacity `6`.

---

## Solution Code

<details>
<summary>Java Solution</summary>

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class CF116ATram {

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(in.readLine());
        int capacity = 0;
        int passengers = 0;
        int a, b;
        String[] p;
        while (n-- > 0) {
            p = in.readLine().split("\\s+");
            a = Integer.parseInt(p[0]);
            b = Integer.parseInt(p[1]);
            passengers -= a;
            passengers += b;
            capacity = Math.max(passengers, capacity);
        }
        out.print(capacity);
        out.close();
    }
}
```

</details>

<details>
<summary>Python Solution</summary>

```python
def solve():
    n = int(input())
    passengers = 0
    capacity = 0

    for _ in range(n):
        leaving, entering = map(int, input().split())
        passengers -= leaving
        passengers += entering
        capacity = max(capacity, passengers)

    print(capacity)


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
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)

	passengers := 0
	capacity := 0

	for ; n > 0; n-- {
		var leaving, entering int
		fmt.Fscan(in, &leaving, &entering)

		passengers -= leaving
		passengers += entering
		if passengers > capacity {
			capacity = passengers
		}
	}

	fmt.Fprintln(out, capacity)
}
```

</details>

---

## Key Takeaways

- When a problem asks for a minimum required capacity, it often reduces to tracking a maximum prefix state.
- A running counter plus a running maximum can solve many simulation problems in one pass.
- Simple implementation problems still benefit from carefully following the order of events in the statement.

---

## Related Problems

- [266B - Queue at the School](https://codeforces.com/problemset/problem/266/B)
- [467A - George and Accommodation](https://codeforces.com/problemset/problem/467/A)
- [1030A - In Search of an Easy Problem](https://codeforces.com/problemset/problem/1030/A)
