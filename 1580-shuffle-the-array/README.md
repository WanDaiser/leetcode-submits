# 1580. Shuffle The Array

- Problem statement: [`1580-shuffle-the-array.md`](./1580-shuffle-the-array.md)
- Referenced submission: [`2025-11-17 14.43.01 - Accepted - runtime 42ms - memory 12.5MB.py`](./2025-11-17 14.43.01 - Accepted - runtime 42ms - memory 12.5MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(n)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(n)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def shuffle(self, nums, n):`
- Loop step: `for i in range(n):`
- Data-structure operation: `ans.append(nums[i])`
- Data-structure operation: `ans.append(nums[i+n])`
- Return path: `return ans`

## Note

This file is auto-generated from your currently accepted submission code.
