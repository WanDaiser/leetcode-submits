# 283. Move Zeroes

- Problem statement: [`283-move-zeroes.md`](./283-move-zeroes.md)
- Referenced submission: [`2025-10-24 03.59.26 - Accepted - runtime 23ms - memory 13.3MB.py`](./2025-10-24 03.59.26 - Accepted - runtime 23ms - memory 13.3MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Stack usage
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def moveZeroes(self, nums):`
- Conditional check: `if len(nums)!=1:`
- Loop step: `while i<len(nums):`
- Conditional check: `if nums[i]==0:`
- Data-structure operation: `nums.pop(i)`
- Conditional check: `else:`

## Note

This file is auto-generated from your currently accepted submission code.
