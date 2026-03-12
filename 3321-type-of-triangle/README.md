# 3321. Type Of Triangle

- Problem statement: [`3321-type-of-triangle.md`](./3321-type-of-triangle.md)
- Referenced submission: [`2025-10-13 22.22.54 - Accepted - runtime 0ms - memory 12.6MB.py`](./2025-10-13 22.22.54 - Accepted - runtime 0ms - memory 12.6MB.py)
- Language: **Python**

## Approach

- Direct conditional / arithmetic implementation

## Step-by-Step Code Walkthrough

- Function signature: `def triangleType(self, nums):`
- Conditional check: `if nums[0]+nums[1]>nums[2] and nums[2]+nums[1]>nums[0] and nums[0]+nums[2]>nums[1]:`
- Conditional check: `if (nums[0]==nums[2]==nums[1]):`
- Return path: `return "equilateral"`
- Conditional check: `elif nums[0]==nums[2] or nums[0]==nums[1] or nums[1]==nums[2]:`
- Return path: `return "isosceles"`
- Conditional check: `else:`
- Return path: `return "scalene"`

## Note

This file is auto-generated from your currently accepted submission code.
