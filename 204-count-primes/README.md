# 204. Count Primes

- Problem statement: [`204-count-primes.md`](./204-count-primes.md)
- Referenced submission: [`2025-11-16 23.53.54 - Accepted - runtime 683ms - memory 101.8MB.py`](./2025-11-16 23.53.54 - Accepted - runtime 683ms - memory 101.8MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def countPrimes(self, n):`
- Conditional check: `if n < 3:`
- Return path: `return 0`
- Loop step: `for i in range(2, limit + 1):`
- Conditional check: `if sieve[i]:`
- Return path: `return sum(sieve)`

## Note

This file is auto-generated from your currently accepted submission code.
