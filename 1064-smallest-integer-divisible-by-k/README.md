# 1064. Smallest Integer Divisible By K

- Problem statement: [`1064-smallest-integer-divisible-by-k.md`](./1064-smallest-integer-divisible-by-k.md)
- Referenced submission: [`2025-11-16 15.43.38 - Accepted - runtime 7ms - memory 12.4MB.py`](./2025-11-16 15.43.38 - Accepted - runtime 7ms - memory 12.4MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def smallestRepunitDivByK(self, k):`
- Conditional check: `if k % 2 == 0 or k % 5 == 0:`
- Return path: `return -1`
- Loop step: `while True:`
- Conditional check: `if curr == 0:`
- Return path: `return length`

## Note

This file is auto-generated from your currently accepted submission code.
