# 628. Maximum Product Of Three Numbers

- Problem statement: [`628-maximum-product-of-three-numbers.md`](./628-maximum-product-of-three-numbers.md)
- Referenced submission: [`2025-11-07 20.24.45 - Accepted - runtime 0ms - memory 13.3MB.py`](./2025-11-07 20.24.45 - Accepted - runtime 0ms - memory 13.3MB.py)
- Language: **Python**

## Approach

- Sorting-based approach
- Dynamic programming / memoization

## Step-by-Step Code Walkthrough

- Function signature: `def maximumProduct(self, nums):`
- Return path: `return max(nums[0]*nums[1]*nums[-1],nums[-3]*nums[-2]*nums[-1])`

## Note

This file is auto-generated from your currently accepted submission code.
