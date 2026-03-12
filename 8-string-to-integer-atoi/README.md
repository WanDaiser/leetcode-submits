# 8. String To Integer Atoi

- Problem statement: [`8-string-to-integer-atoi.md`](./8-string-to-integer-atoi.md)
- Referenced submission: [`2025-11-08 01.35.28 - Accepted - runtime 0ms - memory 12.6MB.py`](./2025-11-08 01.35.28 - Accepted - runtime 0ms - memory 12.6MB.py)
- Language: **Python**

## Approach

- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def myAtoi(self, s):`
- Loop step: `while i < n and s[i] == ' ' :`
- Conditional check: `if i == n :`
- Return path: `return 0`
- Conditional check: `if s[i] == '+' or s[i] == '-' :`
- Conditional check: `if s[i] == '-' :`
- Loop step: `while i < n and s[i].isdigit() :`
- Conditional check: `if num < -2**31 :`

## Note

This file is auto-generated from your currently accepted submission code.
