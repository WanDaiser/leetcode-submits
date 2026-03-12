# 1260. Day Of The Year

- Problem statement: [`1260-day-of-the-year.md`](./1260-day-of-the-year.md)
- Referenced submission: [`2025-10-17 22.02.05 - Accepted - runtime 33ms - memory 12.4MB.py`](./2025-10-17 22.02.05 - Accepted - runtime 33ms - memory 12.4MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def dayOfYear(self, date):`
- Function signature: `def artikyil(n):`
- Conditional check: `if n%4==0:`
- Conditional check: `if n%100==0 and n%400!=0:`
- Return path: `return False`
- Conditional check: `else:`
- Return path: `return True`
- Conditional check: `if artikyil(int(a[0])) and int(a[1])>2:`

## Note

This file is auto-generated from your currently accepted submission code.
