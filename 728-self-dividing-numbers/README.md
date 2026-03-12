# 728. Self Dividing Numbers

- Problem statement: [`728-self-dividing-numbers.md`](./728-self-dividing-numbers.md)
- Referenced submission: [`2025-11-16 16.20.27 - Accepted - runtime 23ms - memory 12.6MB.py`](./2025-11-16 16.20.27 - Accepted - runtime 23ms - memory 12.6MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(n)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(n)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Hash-table based lookup
- Two-pointer style traversal
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def selfDividingNumbers(self, left, right):`
- Function signature: `def selfdiv(a):`
- Loop step: `for ch in str(a):`
- Conditional check: `if d == 0 or a % d != 0:`
- Return path: `return False`
- Return path: `return True`
- Loop step: `for i in range(left, right + 1):`
- Conditional check: `if selfdiv(i):`

## Note

This file is auto-generated from your currently accepted submission code.
