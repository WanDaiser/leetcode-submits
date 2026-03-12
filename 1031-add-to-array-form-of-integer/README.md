# 1031. Add To Array Form Of Integer

- Problem statement: [`1031-add-to-array-form-of-integer.md`](./1031-add-to-array-form-of-integer.md)
- Referenced submission: [`2025-10-19 07.10.33 - Accepted - runtime 63ms - memory 12.6MB.py`](./2025-10-19 07.10.33 - Accepted - runtime 63ms - memory 12.6MB.py)
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

- Function signature: `def addToArrayForm(self, num, k):`
- Data-structure operation: `a=int("".join(map(str,num)))+k`
- Return path: `return [int(s) for s in str(a)]`

## Note

This file is auto-generated from your currently accepted submission code.
