# 1421. Find Numbers With Even Number Of Digits

- Problem statement: [`1421-find-numbers-with-even-number-of-digits.md`](./1421-find-numbers-with-even-number-of-digits.md)
- Referenced submission: [`2025-11-09 00.20.22 - Accepted - runtime 3ms - memory 12.3MB.py`](./2025-11-09 00.20.22 - Accepted - runtime 3ms - memory 12.3MB.py)
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

- Function signature: `def findNumbers(self, nums):`
- Loop step: `for num in nums:`
- Conditional check: `if len(str(num))%2==0:`
- Return path: `return c`

## Note

This file is auto-generated from your currently accepted submission code.
