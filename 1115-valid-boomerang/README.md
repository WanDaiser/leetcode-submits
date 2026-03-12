# 1115. Valid Boomerang

- Problem statement: [`1115-valid-boomerang.md`](./1115-valid-boomerang.md)
- Referenced submission: [`2025-11-03 20.23.08 - Accepted - runtime 0ms - memory 12.5MB.py`](./2025-11-03 20.23.08 - Accepted - runtime 0ms - memory 12.5MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(1)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(1)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Direct conditional / arithmetic implementation

## Step-by-Step Code Walkthrough

- Function signature: `def isBoomerang(self, p):`
- Conditional check: `if p[0] == p[1] or p[1] == p[2] or p[0] == p[2]:`
- Return path: `return False`
- Return path: `return (p[1][1] - p[0][1]) * (p[2][0] - p[1][0]) != (p[2][1] - p[1][1]) * (p[1][0] - p[0][0])`

## Note

This file is auto-generated from your currently accepted submission code.
