# 🧠 Algorithmic Patterns Guide

Master these 15 patterns and you can solve 90% of interview problems.

---

## 1. 🔄 Two Pointers

**When:** Sorted arrays, finding pairs, removing duplicates
**Key Idea:** Two indices moving toward each other or in same direction

```
Example: Two Sum (sorted array)
Left → ← Right
If sum < target: move left →
If sum > target: move right ←
```

**Problems:** Two Sum, Container With Most Water, 3Sum

---

## 2. 🪟 Sliding Window

**When:** Contiguous subarray/substring with constraint
**Key Idea:** Expand right, shrink left, maintain window state

```
[  window  ]
   ←→ expand/shrink
```

**Problems:** Max Sum Subarray, Longest Substring Without Repeating

---

## 3. 🔍 Binary Search

**When:** Sorted data, monotonic function, optimization
**Key Idea:** Halve search space each step

```
lo = 0, hi = n-1
while lo <= hi:
    mid = (lo + hi) / 2
    if condition: hi = mid - 1
    else: lo = mid + 1
```

**Problems:** Search Rotated Array, Koko Eating Bananas

---

## 4. 🌊 BFS (Breadth-First Search)

**When:** Shortest path (unweighted), level-order traversal
**Key Idea:** Process nodes level by level using queue

**Problems:** Number of Islands, Shortest Path, Word Ladder

---

## 5. 🏔️ DFS (Depth-First Search)

**When:** Exploring all paths, connected components, tree traversal
**Key Idea:** Go deep, backtrack, explore next branch

**Problems:** Path Sum, Number of Islands, Clone Graph

---

## 6. 📦 Dynamic Programming

**When:** Overlapping subproblems + optimal substructure
**Key Idea:** Store results of subproblems, build up to solution

### Framework
1. Define state: `dp[i]` = ?
2. Base case: `dp[0]` = ?
3. Transition: `dp[i] = f(dp[i-1], ...)`
4. Answer: `dp[n]`

**Problems:** Fibonacci, Knapsack, Longest Common Subsequence, Coin Change

---

## 7. 🎒 Greedy

**When:** Local optimal choice leads to global optimal
**Key Idea:** Always pick the best option at each step

**Proof technique:** Exchange argument — show greedy ≥ any other solution

**Problems:** Activity Selection, Jump Game, Task Scheduler

---

## 8. 🔙 Backtracking

**When:** Generate all valid combinations/permutations
**Key Idea:** Build incrementally, abandon invalid paths early

```
backtrack(choices, path):
    if valid(path): add to results
    for choice in choices:
        if isValid(choice):
            path.add(choice)
            backtrack(remaining, path)
            path.remove(choice)  # undo
```

**Problems:** N-Queens, Sudoku Solver, Subsets, Permutations

---

## 9. 🏗️ Stack

**When:** Nested structure, matching brackets, monotonic conditions
**Key Idea:** LIFO — process most recent first

**Monotonic Stack:** Find next greater/smaller element in O(n)

**Problems:** Valid Parentheses, Daily Temperatures, Largest Rectangle

---

## 10. 📊 Heap / Priority Queue

**When:** Repeatedly finding min/max, top-K elements
**Key Idea:** O(log n) insert/remove, O(1) peek

**Problems:** Kth Largest Element, Merge K Sorted Lists, Median Finder

---

## 11. 🔗 Union Find (Disjoint Set)

**When:** Connected components, cycle detection, grouping
**Key Idea:** Track parent of each node, path compression + union by rank

**Problems:** Number of Connected Components, Redundant Connection

---

## 12. 📚 Trie (Prefix Tree)

**When:** Prefix-based search, autocomplete, word dictionary
**Key Idea:** Tree where each edge represents a character

**Problems:** Implement Trie, Word Search II, Autocomplete

---

## 13. 🗺️ Topological Sort

**When:** Dependency ordering, course scheduling
**Key Idea:** Process nodes with no dependencies first (Kahn's algorithm)

**Problems:** Course Schedule, Alien Dictionary, Build Order

---

## 14. 🔢 Bit Manipulation

**When:** Sets, toggles, power of 2, XOR tricks
**Key Tricks:**
- `x & (x-1)` removes lowest set bit
- `x ^ x = 0` (find single number)
- `x & 1` checks odd/even

**Problems:** Single Number, Counting Bits, Power of Two

---

## 15. 📐 Divide and Conquer

**When:** Problem breaks into similar smaller subproblems
**Key Idea:** Split → Solve → Merge

**Problems:** Merge Sort, Quick Select, Closest Pair of Points

---

## 🗺️ Pattern Selection Flowchart

```
Input is sorted? → Binary Search or Two Pointers
Finding shortest path? → BFS
Exploring all options? → DFS or Backtracking
Optimal substructure? → DP or Greedy
Need top-K? → Heap
Matching/nesting? → Stack
Prefix operations? → Trie
Dependencies? → Topological Sort
Grouping/connectivity? → Union Find
```
