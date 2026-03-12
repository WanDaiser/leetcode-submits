# 507. Perfect Number

- Problem statement: [`507-perfect-number.md`](./507-perfect-number.md)
- Referenced submission: [`2025-10-14 01.41.18 - Accepted - runtime 8ms - memory 12.4MB.py`](./2025-10-14 01.41.18 - Accepted - runtime 8ms - memory 12.4MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def checkPerfectNumber(self, num):`
- Conditional check: `if num <= 1:`
- Return path: `return False`
- Loop step: `while i * i <= num:`
- Conditional check: `if num % i == 0:`
- Conditional check: `if i != num // i:`
- Return path: `return s == num`

## Note

This file is auto-generated from your currently accepted submission code.
