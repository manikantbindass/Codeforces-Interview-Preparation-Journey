# Watermelon

> **Difficulty:** Easy | **Rating:** 800 | **Tags:** `math`, `brute-force`
> **Date Solved:** 2026-04-20

---

## 🔗 Problem Link

[4A — Watermelon — Codeforces](https://codeforces.com/problemset/problem/4/A)

---

## 💡 Approach

### Intuition
Pete and Billy want to divide a watermelon into two parts, each weighing an even number of kilos. We need to check if this is possible.

### Optimized Logic
A watermelon of weight `w` can be divided into two even parts if and only if:
1. `w` is even (otherwise can't split into two even numbers)
2. `w > 2` (because `w = 2` would give parts of 0 and 2, and 0 is not valid)

So the answer is `YES` if `w` is even AND `w > 2`, otherwise `NO`.

---

## 🧠 Concepts Used

- **Data Structures:** None (pure math)
- **Algorithms:** Number theory basics
- **Patterns:** Mathematical reasoning, parity check

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
8
```

### Output
```
YES
```

### Explanation
8 can be split into 2 + 6, or 4 + 4. Both parts even. → YES.

---

## ✅ Solution Code

<details>
<summary>C++ Solution</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int w;
    cin >> w;
    if (w % 2 == 0 && w > 2)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}
```

</details>

<details>
<summary>Python Solution</summary>

```python
w = int(input())
print("YES" if w % 2 == 0 and w > 2 else "NO")
```

</details>

<details>
<summary>Java Solution</summary>

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int w = sc.nextInt();
        System.out.println(w % 2 == 0 && w > 2 ? "YES" : "NO");
    }
}
```

</details>

---

## 📌 Key Takeaways

- Simplest problems test mathematical reasoning
- Always consider edge cases (w=1, w=2)
- Parity is fundamental concept in number theory problems

---

## 🔗 Related Problems

- [4B — Before an Exam](https://codeforces.com/problemset/problem/4/B)
- [4C — Registration System](https://codeforces.com/problemset/problem/4/C)
