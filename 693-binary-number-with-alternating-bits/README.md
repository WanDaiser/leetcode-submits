# 693. Binary Number With Alternating Bits

- Problem statement: [`693-binary-number-with-alternating-bits.md`](./693-binary-number-with-alternating-bits.md)
- Referenced submission: [`2026-02-22 19.09.04 - Accepted - runtime 0ms - memory 12.6MB.py`](./2026-02-22 19.09.04 - Accepted - runtime 0ms - memory 12.6MB.py)
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

- Function signature: `def hasAlternatingBits(self, n):`
- Loop step: `for i in range(1,len(b)):`
- Conditional check: `if b[i]==b[i-1]:`
- Return path: `return False`
- Return path: `return True`

## Note

This file is auto-generated from your currently accepted submission code.
