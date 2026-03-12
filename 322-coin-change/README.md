# 322. Coin Change

- Problem statement: [`322-coin-change.md`](./322-coin-change.md)
- Referenced submission: [`2025-10-14 17.21.59 - Accepted - runtime 788ms - memory 13.1MB.py`](./2025-10-14 17.21.59 - Accepted - runtime 788ms - memory 13.1MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Dynamic programming / memoization
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def coinChange(self, coins, amount):`
- Loop step: `for i in range(1, amount + 1):`
- Loop step: `for coin in coins:`
- Conditional check: `if coin <= i:`
- Return path: `return -1 if dp[amount] > amount else dp[amount]`

## Note

This file is auto-generated from your currently accepted submission code.
