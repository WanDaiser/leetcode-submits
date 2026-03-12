# 202. Happy Number

- Problem statement: [`202-happy-number.md`](./202-happy-number.md)
- Referenced submission: [`2025-10-17 00.09.54 - Accepted - runtime 7ms - memory 12.3MB.py`](./2025-10-17 00.09.54 - Accepted - runtime 7ms - memory 12.3MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n^2)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(n)-teal)

## Complexity (Estimated)

- Time: **~O(n^2)**
- Space: **~O(n)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def isHappy(self, n):`
- Data-structure operation: `seen = set()`
- Loop step: `while n != 1:`
- Conditional check: `if n in seen:`
- Return path: `return False`
- Data-structure operation: `seen.add(n)`
- Loop step: `for digit in a:`
- Return path: `return True`

## Note

This file is auto-generated from your currently accepted submission code.
