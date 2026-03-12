# 1349. Check If It Is A Straight Line

- Problem statement: [`1349-check-if-it-is-a-straight-line.md`](./1349-check-if-it-is-a-straight-line.md)
- Referenced submission: [`2025-11-07 18.14.44 - Accepted - runtime 0ms - memory 12.7MB.py`](./2025-11-07 18.14.44 - Accepted - runtime 0ms - memory 12.7MB.py)
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

- Function signature: `def checkStraightLine(self, c):`
- Return path: `return all((c[i+1][1]-c[i][1])*(c[i+2][0]-c[i+1][0]) == (c[i+2][1]-c[i+1][1])*(c[i+1][0]-c[i][0]) for i in range(len(c)-2))`

## Note

This file is auto-generated from your currently accepted submission code.
