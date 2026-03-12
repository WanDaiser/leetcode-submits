# 2752. Sum Multiples

- Problem statement: [`2752-sum-multiples.md`](./2752-sum-multiples.md)
- Referenced submission: [`2025-10-22 03.53.16 - Accepted - runtime 41ms - memory 12.4MB.py`](./2025-10-22 03.53.16 - Accepted - runtime 41ms - memory 12.4MB.py)
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

- Function signature: `def sumOfMultiples(self, n):`
- Loop step: `for i in range(n+1):`
- Conditional check: `if i%3==0 or i%5==0 or i%7==0:`
- Return path: `return ans`

## Note

This file is auto-generated from your currently accepted submission code.
