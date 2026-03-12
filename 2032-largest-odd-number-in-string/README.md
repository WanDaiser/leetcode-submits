# 2032. Largest Odd Number In String

- Problem statement: [`2032-largest-odd-number-in-string.md`](./2032-largest-odd-number-in-string.md)
- Referenced submission: [`2025-10-30 15.18.37 - Accepted - runtime 40ms - memory 17.1MB.py`](./2025-10-30 15.18.37 - Accepted - runtime 40ms - memory 17.1MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def largestOddNumber(self, num):`
- Loop step: `for i in range(len(num) - 1, -1, -1):`
- Conditional check: `if int(num[i]) % 2 == 1:`
- Return path: `return num[:i + 1]`
- Return path: `return ""`

## Note

This file is auto-generated from your currently accepted submission code.
