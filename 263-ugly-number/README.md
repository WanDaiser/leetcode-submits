# 263. Ugly Number

- Problem statement: [`263-ugly-number.md`](./263-ugly-number.md)
- Referenced submission: [`2025-11-16 15.24.58 - Accepted - runtime 0ms - memory 12.4MB.py`](./2025-11-16 15.24.58 - Accepted - runtime 0ms - memory 12.4MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def isUgly(self, n):`
- Conditional check: `if n <= 0:`
- Return path: `return False`
- Loop step: `for p in [2, 3, 5]:`
- Loop step: `while n % p == 0:`
- Return path: `return n == 1`

## Note

This file is auto-generated from your currently accepted submission code.
