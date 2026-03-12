# 504. Base 7

- Problem statement: [`504-base-7.md`](./504-base-7.md)
- Referenced submission: [`2025-11-06 20.06.12 - Accepted - runtime 0ms - memory 12.5MB.py`](./2025-11-06 20.06.12 - Accepted - runtime 0ms - memory 12.5MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(1)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(1)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Direct conditional / arithmetic implementation

## Step-by-Step Code Walkthrough

- Function signature: `def convertToBase7(self, num):`
- Conditional check: `if num <0:`
- Return path: `return "-"+self.convertToBase7(-num)`
- Return path: `return str(num) if -7 < num < 7 else self.convertToBase7(num//7)+str(num%7)`

## Note

This file is auto-generated from your currently accepted submission code.
