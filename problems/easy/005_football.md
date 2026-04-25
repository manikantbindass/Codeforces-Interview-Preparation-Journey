# Football

> **Difficulty:** Easy | **Rating:** 900 | **Tags:** `implementation`, `strings`
> **Date Solved:** 2026-04-25

---

## Problem Link

[96A - Football - Codeforces](https://codeforces.com/problemset/problem/96/A)

---

## Approach

### Intuition
The input is a binary string showing the current order of players from two teams. The situation becomes dangerous if either team has at least 7 players standing consecutively, so we only need to check whether the string contains `0000000` or `1111111`.

### Optimized Logic

1. Read the string of player positions.
2. Check whether it contains 7 consecutive zeroes.
3. Check whether it contains 7 consecutive ones.
4. Print `YES` if either pattern exists; otherwise print `NO`.

### Why This Works
Any dangerous situation must include a run of length 7 made of the same character. Since the string only contains `0` and `1`, searching directly for `0000000` and `1111111` covers every valid dangerous case.

---

## Concepts Used

- **Data Structures:** String
- **Algorithms:** Substring search
- **Patterns:** Linear scan, implementation

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
1000000001
```

### Output
```text
YES
```

### Explanation
The string contains `0000000`, so one team has at least 7 players in a row and the situation is dangerous.

### Input
```text
001001
```

### Output
```text
NO
```

### Explanation
There is no run of 7 equal characters, so the situation is not dangerous.

---

## Solution Code

<details>
<summary>C++ Solution</summary>

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string players;
    cin >> players;

    if (players.find("0000000") != string::npos || players.find("1111111") != string::npos) {
        cout << "YES";
    } else {
        cout << "NO";
    }

    return 0;
}
```

</details>

<details>
<summary>Java Solution</summary>

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
public class CF096AFootball {

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        String players = in.readLine();
        out.print(players.contains("0000000") || players.contains("1111111") ? "YES" : "NO");
        out.close();
    }
}
```

</details>

<details>
<summary>Python Solution</summary>

```python
def solve():
    players = input().strip()
    if "0000000" in players or "1111111" in players:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
```

</details>

---

## Key Takeaways

- Fixed-length pattern checks can make implementation problems very direct.
- When the alphabet is tiny, searching for the exact dangerous patterns is often simpler than manual counting.
- For short strings, a clean built-in string check is both readable and efficient.

---

## Related Problems

- [58A - Chat room](https://codeforces.com/problemset/problem/58/A)
- [118A - String Task](https://codeforces.com/problemset/problem/118/A)
- [96B - Lucky Numbers (easy)](https://codeforces.com/problemset/problem/96/B)
