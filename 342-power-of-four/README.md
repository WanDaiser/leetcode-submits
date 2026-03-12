# 342. Power Of Four

- Problem statement: [`342-power-of-four.md`](./342-power-of-four.md)
- Referenced submission: [`2025-10-13 22.39.46 - Accepted - runtime 0ms - memory 12.4MB.py`](./2025-10-13 22.39.46 - Accepted - runtime 0ms - memory 12.4MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(1)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(1)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Direct conditional / arithmetic implementation

## Step-by-Step Code Walkthrough

- Function signature: `def isPowerOfFour(self, n):`
- Return path: `return (True if n>0 and ( n & (n-1)) == 0 and n%3==1 else False)`

## Note

This file is auto-generated from your currently accepted submission code.
