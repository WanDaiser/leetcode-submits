# 29. Divide Two Integers

- Problem statement: [`29-divide-two-integers.md`](./29-divide-two-integers.md)
- Referenced submission: [`2025-08-24 16.15.44 - Accepted - runtime 0ms - memory 12.6MB.py`](./2025-08-24 16.15.44 - Accepted - runtime 0ms - memory 12.6MB.py)
- Language: **Python**

## Approach

- Direct conditional / arithmetic implementation

## Step-by-Step Code Walkthrough

- Function signature: `def divide(self, dividend, divisor):`
- Conditional check: `if (dividend < 0) != (divisor < 0):`
- Return path: `return max(min(quotient, 2**31 - 1), -2**31)`

## Note

This file is auto-generated from your currently accepted submission code.
