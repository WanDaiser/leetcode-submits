# 1996. Number Of Ways To Rearrange Sticks With K Sticks Visible

- Problem statement: [`1996-number-of-ways-to-rearrange-sticks-with-k-sticks-visible.md`](./1996-number-of-ways-to-rearrange-sticks-with-k-sticks-visible.md)
- Referenced submission: [`2025-11-16 17.18.07 - Accepted - runtime 893ms - memory 32.4MB.py`](./2025-11-16 17.18.07 - Accepted - runtime 893ms - memory 32.4MB.py)
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

- Function signature: `def rearrangeSticks(self, n, k):`
- Loop step: `for i in range(1, n+1):`
- Loop step: `for j in range(1, min(i, k)+1):`
- Return path: `return dp[n][k]`

## Note

This file is auto-generated from your currently accepted submission code.
