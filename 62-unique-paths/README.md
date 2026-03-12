# 62. Unique Paths

- Problem statement: [`62-unique-paths.md`](./62-unique-paths.md)
- Referenced submission: [`2025-10-16 20.54.47 - Accepted - runtime 0ms - memory 12.5MB.py`](./2025-10-16 20.54.47 - Accepted - runtime 0ms - memory 12.5MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n^2)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(n^2)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Hash-table based lookup
- Dynamic programming / memoization
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def uniquePaths(self, m, n):`
- Loop step: `for i in range(m):`
- Loop step: `for j in range(n):`
- Conditional check: `if i==0 or j==0:`
- Conditional check: `else:`
- Return path: `return dp[(m-1,n-1)]`

## Note

This file is auto-generated from your currently accepted submission code.
