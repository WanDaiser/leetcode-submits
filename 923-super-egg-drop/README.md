# 923. Super Egg Drop

- Problem statement: [`923-super-egg-drop.md`](./923-super-egg-drop.md)
- Referenced submission: [`2025-11-14 23.00.15 - Accepted - runtime 0ms - memory 12.5MB.py`](./2025-11-14 23.00.15 - Accepted - runtime 0ms - memory 12.5MB.py)
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

- Function signature: `def superEggDrop(self, k, n):`
- Loop step: `while dp[k]<n:`
- Loop step: `for x in range(k, 0, -1):`
- Return path: `return m`

## Note

This file is auto-generated from your currently accepted submission code.
