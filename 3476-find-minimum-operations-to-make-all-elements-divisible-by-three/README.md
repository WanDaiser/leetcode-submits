# 3476. Find Minimum Operations To Make All Elements Divisible By Three

- Problem statement: [`3476-find-minimum-operations-to-make-all-elements-divisible-by-three.md`](./3476-find-minimum-operations-to-make-all-elements-divisible-by-three.md)
- Referenced submission: [`2026-01-02 01.31.21 - Accepted - runtime 0ms - memory 12.6MB.py`](./2026-01-02 01.31.21 - Accepted - runtime 0ms - memory 12.6MB.py)
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

- Function signature: `def minimumOperations(self, nums):`
- Return path: `return sum(1 for n in nums if n% 3)`

## Note

This file is auto-generated from your currently accepted submission code.
