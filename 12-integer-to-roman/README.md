# 12. Integer To Roman

- Problem statement: [`12-integer-to-roman.md`](./12-integer-to-roman.md)
- Referenced submission: [`2026-03-12 13.00.09 - Accepted - runtime 12ms - memory 12.5MB.py`](./2026-03-12 13.00.09 - Accepted - runtime 12ms - memory 12.5MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n%20log%20n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(n log n)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Hash-table based lookup
- Sorting-based approach
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def intToRoman(self, num):`
- Loop step: `for v,sym in sorted(rv.items(),reverse=True):`
- Return path: `return rm`

## Note

This file is auto-generated from your currently accepted submission code.
