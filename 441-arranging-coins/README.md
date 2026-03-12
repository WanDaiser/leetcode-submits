# 441. Arranging Coins

- Problem statement: [`441-arranging-coins.md`](./441-arranging-coins.md)
- Referenced submission: [`2025-10-31 00.40.23 - Accepted - runtime 713ms - memory 12.3MB.py`](./2025-10-31 00.40.23 - Accepted - runtime 713ms - memory 12.3MB.py)
- Language: **Python**

## Approach

- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def arrangeCoins(self, n):`
- Conditional check: `if n==1 or n==2:`
- Return path: `return 1`
- Conditional check: `elif n==3:`
- Return path: `return 2`
- Loop step: `while a<n:`
- Conditional check: `if (((a+1)*a)/2)>n:`
- Return path: `return a-1`

## Note

This file is auto-generated from your currently accepted submission code.
