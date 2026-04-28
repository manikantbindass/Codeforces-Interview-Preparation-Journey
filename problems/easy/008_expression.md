# Expression

> **Difficulty:** Easy | **Rating:** 1000 | **Tags:** `brute-force`, `math`
> **Date Solved:** 2026-04-28

---

## Problem Link

[479A - Expression - Codeforces](https://codeforces.com/problemset/problem/479/A)

---

## Approach

### Intuition
There are only two operator positions and only `+`, `*`, and parentheses can be used without changing the order of `a`, `b`, and `c`. So instead of searching for a pattern, we can directly evaluate every valid expression form and take the maximum.

### Optimized Logic

1. Read the three integers `a`, `b`, and `c`.
2. Compute all six valid outcomes:
   `a + b + c`, `a * b * c`, `a * b + c`, `a + b * c`, `a * (b + c)`, `(a + b) * c`.
3. Return the largest of those values.

### Why This Works
Since the order of numbers cannot change, every maximum-producing expression must be one of those six forms. Checking all of them guarantees we do not miss the optimal answer.

---

## Concepts Used

- **Data Structures:** Fixed-size array / variables
- **Algorithms:** Direct enumeration
- **Patterns:** Brute force, expression evaluation, math

---

## Complexity

| Metric | Value |
|--------|-------|
| **Time** | O(1) |
| **Space** | O(1) |

---

## Example

### Input
```text
1
2
3
```

### Output
```text
9
```

### Explanation
The best expression is `(1 + 2) * 3 = 9`, which is larger than the other valid combinations.

### Input
```text
2
10
3
```

### Output
```text
60
```

### Explanation
The largest value comes from `2 * 10 * 3 = 60`, so the answer is `60`.

---

## Solution Code

<details>
<summary>Java Solution</summary>

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.Closeable;
import java.io.Flushable;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class CF479AExpression {

    static Reader in = new Reader(System.in);
    static Writer out = new Writer(System.out);

    public static void main(String[] args) throws IOException {

        int a = in.nextInt();
        int b = in.nextInt();
        int c = in.nextInt();
        int[] answers = new int[6];
        answers[0] = a + b + c;
        answers[1] = a * b * c;
        answers[2] = a * b + c;
        answers[3] = a + b * c;
        answers[4] = a * (b + c);
        answers[5] = (a + b) * c;
        Arrays.sort(answers);
        int max = answers[5];
        out.println(max);
        in.close();
        out.flush();
        out.close();
    }

    static class Reader implements Closeable {

        private final BufferedReader reader;
        private StringTokenizer tokenizer;

        public Reader(InputStream input) {
            reader = new BufferedReader(new InputStreamReader(input));
            tokenizer = new StringTokenizer("");
        }

        private StringTokenizer getTokenizer() throws IOException {
            if (tokenizer == null || !tokenizer.hasMoreTokens()) {
                String line = nextLine();
                if (line == null) {
                    return null;
                }
                tokenizer = new StringTokenizer(line);
            }
            return tokenizer;
        }

        public boolean hasNext() throws IOException {
            return getTokenizer() != null;
        }

        public String next() throws IOException {
            return hasNext() ? tokenizer.nextToken() : null;
        }

        public String nextLine() throws IOException {
            tokenizer = null;
            return reader.readLine();
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

        public long nextLong() throws IOException {
            return Long.parseLong(next());
        }

        public float nextFloat() throws IOException {
            return Float.parseFloat(next());
        }

        public double nextDouble() throws IOException {
            return Double.parseDouble(next());
        }

        public String[] nextStringArray(int size) throws IOException {
            String[] array = new String[size];
            for (int i = 0; i < size; i++) {
                array[i] = next();
            }
            return array;
        }

        public int[] nextIntArray(int size) throws IOException {
            int[] array = new int[size];
            for (int i = 0; i < size; i++) {
                array[i] = nextInt();
            }
            return array;
        }

        public long[] nextLongArray(int size) throws IOException {
            long[] array = new long[size];
            for (int i = 0; i < size; i++) {
                array[i] = nextLong();
            }
            return array;
        }

        public double[] nextDoubleArray(int size) throws IOException {
            double[] array = new double[size];
            for (int i = 0; i < size; i++) {
                array[i] = nextDouble();
            }
            return array;
        }

        @Override
        public void close() throws IOException {
            tokenizer = null;
            reader.close();
        }
    }

    static class Writer implements Closeable, Flushable {

        private final PrintWriter writer;

        public Writer(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public void print(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                if (i != 0) {
                    writer.print(' ');
                }
                writer.print(objects[i]);
            }
        }

        public void println(Object... objects) {
            print(objects);
            writer.println();
        }

        @Override
        public void close() {
            writer.close();
        }

        @Override
        public void flush() {
            writer.flush();
        }
    }
}
```

</details>

<details>
<summary>Python Solution</summary>

```python
def solve():
    a = int(input())
    b = int(input())
    c = int(input())

    answers = [
        a + b + c,
        a * b * c,
        a * b + c,
        a + b * c,
        a * (b + c),
        (a + b) * c,
    ]

    print(max(answers))


if __name__ == "__main__":
    solve()
```

</details>

<details>
<summary>Go Solution</summary>

```go
package main

import "fmt"

func main() {
	var a, b, c int
	fmt.Scan(&a, &b, &c)

	answers := []int{
		a + b + c,
		a * b * c,
		a*b + c,
		a + b*c,
		a * (b + c),
		(a + b) * c,
	}

	best := answers[0]
	for _, value := range answers {
		if value > best {
			best = value
		}
	}

	fmt.Println(best)
}
```

</details>

---

## Key Takeaways

- When the number of valid expressions is tiny, direct enumeration is often the cleanest solution.
- Parentheses can change the answer dramatically even in very small arithmetic problems.
- Always respect the original order of elements in Codeforces expression problems.

---

## Related Problems

- [4A - Watermelon](https://codeforces.com/problemset/problem/4/A)
- [1A - Theatre Square](https://codeforces.com/problemset/problem/1/A)
- [69A - Young Physicist](https://codeforces.com/problemset/problem/69/A)
