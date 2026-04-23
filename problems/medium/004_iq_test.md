# IQ Test

> **Difficulty:** Medium | **Rating:** 1300 | **Tags:** `brute-force`
> **Date Solved:** 2026-04-23

---

## Problem Link

[25A - IQ Test - Codeforces](https://codeforces.com/problemset/problem/25/A)

---

## Approach

### Intuition
Among the given numbers, exactly one has different parity from the others. So we only need to determine whether the majority is even or odd, then print the index of the outlier.

### Optimized Logic

1. Look at the first three numbers.
2. Their parity is enough to determine the majority parity.
3. Scan the array and find the one number whose parity differs from that majority.
4. Print its 1-based index.

### Why This Works
Because exactly one number differs in evenness, at least two of the first three numbers must belong to the majority parity. That lets us determine which parity is the outlier in constant time, and then a single pass finds its index.

---

## Concepts Used

- **Data Structures:** Array/List
- **Algorithms:** Linear scan
- **Patterns:** Parity check, brute force

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
5
2 4 7 8 10
```

### Output
```text
3
```

### Explanation
Most numbers are even, and `7` is the only odd number. Its 1-based position is `3`.

### Input
```text
4
1 2 1 1
```

### Output
```text
2
```

### Explanation
Most numbers are odd, and `2` is the only even number. Its index is `2`.

---

## Solution Code

<details>
<summary>C++ Solution</summary>

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int even_count = 0;
    for (int i = 0; i < 3; i++) {
        if (nums[i] % 2 == 0) {
            even_count++;
        }
    }

    int majority_parity = (even_count >= 2) ? 0 : 1;

    for (int i = 0; i < n; i++) {
        if (nums[i] % 2 != majority_parity) {
            cout << i + 1 << '\n';
            break;
        }
    }

    return 0;
}
```

</details>

<details>
<summary>Python Solution</summary>

```python
import sys


def solve():
    data = list(map(int, sys.stdin.read().strip().split()))

    n = data[0]
    nums = data[1:]

    a1 = nums[0]
    a2 = nums[1]

    # Case 1: both even -> majority even -> find odd
    if a1 % 2 == 0 and a2 % 2 == 0:
        for i in range(2, n):
            if nums[i] % 2 == 1:
                print(i + 1)
                return

    # Case 2: both odd -> majority odd -> find even
    elif a1 % 2 == 1 and a2 % 2 == 1:
        for i in range(2, n):
            if nums[i] % 2 == 0:
                print(i + 1)
                return

    # Case 3: first two different -> check third
    else:
        a3 = nums[2]
        evenness = a3 % 2
        if a1 % 2 == evenness:
            print(2)
        else:
            print(1)


if __name__ == "__main__":
    solve()
```

</details>

<details>
<summary>Java Solution</summary>

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class CF25AIQTest {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();
        int n = fs.nextInt();
        int[] nums = new int[n];

        for (int i = 0; i < n; i++) {
            nums[i] = fs.nextInt();
        }

        int evenCount = 0;
        for (int i = 0; i < 3; i++) {
            if (nums[i] % 2 == 0) {
                evenCount++;
            }
        }

        int majorityParity = (evenCount >= 2) ? 0 : 1;

        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 != majorityParity) {
                System.out.println(i + 1);
                return;
            }
        }
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

---

## Key Takeaways

- The first three numbers are enough to detect the majority parity.
- Once the majority parity is known, one scan finds the outlier index.
- This is a classic parity observation problem despite the simple implementation.

---

## Related Problems

- [4A - Watermelon](https://codeforces.com/problemset/problem/4/A)
- [313A - Ilya and Bank Account](https://codeforces.com/problemset/problem/313/A)
- [158A - Next Round](https://codeforces.com/problemset/problem/158/A)
