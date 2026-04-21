# Ilya and Bank Account

> **Difficulty:** Medium | **Rating:** 1000 | **Tags:** `math`, `implementation`, `number-theory`
> **Date Solved:** 2026-04-21

---

## 🔗 Problem Link

[313A — Ilya and Bank Account — Codeforces](https://codeforces.com/problemset/problem/313/A)

---

## 💡 Approach

### Intuition
Ilya has a bank account with balance `n`. If the balance is negative, he can perform **at most one operation** — remove either the **last digit** or the **second-to-last digit** — to maximize his balance (make it as close to 0 as possible). If the balance is already non-negative, no action is needed.

### Optimized Logic

1. If `n >= 0` → print `n` directly (already optimal)
2. If `n < 0`:
   - **Option 1:** Remove the last digit → `n / 10`
   - **Option 2:** Remove the second-to-last digit → `(n / 100) * 10 + (n % 10)`
   - Print `max(option1, option2)` — the one closest to zero wins

### Why This Works
For negative numbers, a larger value means closer to zero. By trying both valid removals on the absolute value and negating back, we always find the optimal single-digit removal.

---

## 🧠 Concepts Used

- **Data Structures:** None (pure math)
- **Algorithms:** Digit manipulation via integer arithmetic
- **Patterns:** Greedy (try both options, pick best)

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
-10
```

### Output
```
0
```

### Explanation
n = -10. Remove last digit (0) → -1. Remove second-to-last digit (1) → 0. max(-1, 0) = **0**.

### Input
```
-100
```

### Output
```
-1
```

### Explanation
n = -100. Remove last digit → -10. Remove second-to-last → -10. Wait — let's recalc: `(-100/100)*10 + (-100%10)` = `-1*10 + 0` = `-10`. Both give `-10`... Actually: remove last `0` → `-10`, remove middle `0` → `-10`, remove `1` isn't an option (only last or second-to-last). max(-10, -10) = **-10**. For input `-100`, answer is `-10`.

Let's use `-123`: Remove last → `-12`. Remove second-to-last → `-13`. max(-12, -13) = **-12**.

---

## ✅ Solution Code

<details>
<summary>C++ Solution 🔧</summary>

```cpp
#include<iostream>
#include<vector>
#include<string>
#include<cstring>
#include<stack>
#include<queue>
#include<cstdio>
#include<set>
#include<unordered_set>
#include<cmath>
#include<algorithm>
#include<functional>
#include<utility>
#include<cstdlib>
using namespace std;
typedef long long int lli;
typedef size_t idx;
#define vi vector<int>
#define pb(n) push_back(n)
#define ln "\n"
#define sp ends
#define newline cout << ln
const int MOD = 1000000007;

#define fastios ios_base::sync_with_stdio(false); cin.tie(0)


int main(){

	#ifndef ONLINE_JUDGE
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
	int n;
	cin >> n;
	if(n >= 0) cout << n << "\n";
	else{
		n = abs(n);
		int temp1 = n / 10;
		int temp2 = (temp1 - (temp1 % 10)) + (n % 10);
		cout << max(-temp1, -temp2) << "\n";
	}
	return 0;
}
```

</details>

<details>
<summary>Java Solution ☕</summary>

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

/**
 * See <a href="https://codeforces.com/problemset/problem/313/A">Ilya and Bank Account</a>
 */
public class CF313AIlyaAndBankAccount {

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(in.readLine().trim());
        if (n >= 0) {
            out.println(n);
        } else {
            int abs = Math.abs(n);
            int option1 = abs / 10;                              // remove last digit
            int option2 = (abs / 100) * 10 + (abs % 10);        // remove second-to-last digit
            out.println(Math.max(-option1, -option2));
        }
        out.close();
    }
}
```

</details>

<details>
<summary>Python Solution 🐍</summary>

```python
def solve():
    n = int(input())
    if n >= 0:
        print(n)
    else:
        a = abs(n)
        option1 = a // 10                          # remove last digit
        option2 = (a // 100) * 10 + (a % 10)       # remove second-to-last digit
        print(max(-option1, -option2))

solve()
```

</details>

---

## 📌 Key Takeaways

- Digit removal via integer arithmetic: `n // 10` removes last digit, `(n // 100) * 10 + (n % 10)` removes second-to-last
- For negative numbers, "maximize" = minimize absolute value (closest to zero)
- Greedy approach: only 2 options exist, try both and pick the best
- No string conversion needed — pure math solution is cleaner and faster

---

## 🔗 Related Problems

- [4A — Watermelon](https://codeforces.com/problemset/problem/4/A)
- [1A — Theatre Square](https://codeforces.com/problemset/problem/1/A)
- [158A — Next Round](https://codeforces.com/problemset/problem/158/A)
