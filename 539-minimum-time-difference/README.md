# 539. Minimum Time Difference

- Problem statement: [`539-minimum-time-difference.md`](./539-minimum-time-difference.md)
- Referenced submission: [`2025-10-19 06.09.46 - Accepted - runtime 23ms - memory 15MB.py`](./2025-10-19 06.09.46 - Accepted - runtime 23ms - memory 15MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n%20log%20n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(n)-teal)

## Complexity (Estimated)

- Time: **~O(n log n)**
- Space: **~O(n)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Hash-table based lookup
- Sorting-based approach
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def findMinDifference(self, tp):`
- Loop step: `for t in tp:`
- Data-structure operation: `h,m=map(int,t.split(":"))`
- Data-structure operation: `minutes.append(h*60+m)`
- Loop step: `for i in range(1,len(minutes)):`
- Return path: `return min_fark`

## Note

This file is auto-generated from your currently accepted submission code.
