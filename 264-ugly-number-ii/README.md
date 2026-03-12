# 264. Ugly Number Ii

- Problem statement: [`264-ugly-number-ii.md`](./264-ugly-number-ii.md)
- Referenced submission: [`2025-10-29 16.52.28 - Accepted - runtime 49ms - memory 12.4MB.py`](./2025-10-29 16.52.28 - Accepted - runtime 49ms - memory 12.4MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(n)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(n)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def nthUglyNumber(self, n):`
- Loop step: `while len(ugly) < n:`
- Data-structure operation: `ugly.append(next_ugly)`
- Conditional check: `if next_ugly == next2:`
- Conditional check: `if next_ugly == next3:`
- Conditional check: `if next_ugly == next5:`
- Return path: `return ugly[-1]`

## Note

This file is auto-generated from your currently accepted submission code.
