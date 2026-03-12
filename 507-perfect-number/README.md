# 507. Perfect Number

- Problem statement: [`507-perfect-number.md`](./507-perfect-number.md)
- Referenced submission: [`2025-10-14 01.41.18 - Accepted - runtime 8ms - memory 12.4MB.py`](./2025-10-14 01.41.18 - Accepted - runtime 8ms - memory 12.4MB.py)
- Language: **Python**

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
