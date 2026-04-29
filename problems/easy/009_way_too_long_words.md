# Way Too Long Words

> **Difficulty:** Easy | **Rating:** 800 | **Tags:** `implementation`, `strings`
> **Date Solved:** 2026-04-29

---

## Problem Link

[71A - Way Too Long Words - Codeforces](https://codeforces.com/problemset/problem/71/A)

---

## Approach

### Intuition
If a word has more than 10 characters, we do not need to keep the middle letters. The problem asks us to keep only the first character, the last character, and the count of characters between them.

### Optimized Logic

1. Read the number of test cases `n`.
2. For each word, check its length.
3. If the length is greater than 10, print the abbreviation:
   first letter + `(length - 2)` + last letter.
4. Otherwise, print the word unchanged.

### Why This Works
For every long word, the abbreviation format is defined directly in the statement. Using the first and last letters with the number of skipped middle letters always produces the exact required result.

---

## Concepts Used

- **Data Structures:** Strings
- **Algorithms:** Direct simulation
- **Patterns:** Implementation, string processing

---

## Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(total characters) |
| **Space** | O(1) extra |

---

## Example

### Input
```text
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
```

### Output
```text
word
l10n
i18n
p43s
```

### Explanation
Words with length at most 10 stay the same. Longer words are shortened to:
first letter + number of middle letters + last letter.

---

## Solution Code

<details>
<summary>Java Solution</summary>

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;

public class CF071AWayTooLongWords {

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {

        byte n = Byte.parseByte(in.readLine());
        String s;
        int length;
        while (n-- > 0) {
            s = in.readLine();
            length = s.length();
            if (length > 10) {
                out.println(s.substring(0, 1) + (length - 2) + s.substring(length - 1));
            } else {
                out.println(s);
            }
        }
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

    for _ in range(n):
        word = input().strip()
        if len(word) > 10:
            print(f"{word[0]}{len(word) - 2}{word[-1]}")
        else:
            print(word)


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

	for ; n > 0; n-- {
		var word string
		fmt.Fscan(in, &word)

		if len(word) > 10 {
			fmt.Fprintf(out, "%c%d%c\n", word[0], len(word)-2, word[len(word)-1])
		} else {
			fmt.Fprintln(out, word)
		}
	}
}
```

</details>

---

## Key Takeaways

- Many beginner string problems are pure rule-application once the output format is understood.
- When only the edges of a string matter, you can often avoid building complicated intermediate logic.
- Always translate the statement into a direct formula before overthinking the solution.

---

## Related Problems

- [112A - Petya and Strings](https://codeforces.com/problemset/problem/112/A)
- [59A - Word](https://codeforces.com/problemset/problem/59/A)
- [118A - String Task](https://codeforces.com/problemset/problem/118/A)
