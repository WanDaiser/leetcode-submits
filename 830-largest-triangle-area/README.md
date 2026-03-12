# 830. Largest Triangle Area

- Problem statement: [`830-largest-triangle-area.md`](./830-largest-triangle-area.md)
- Referenced submission: [`2026-02-22 18.38.57 - Accepted - runtime 47ms - memory 12.6MB.py`](./2026-02-22 18.38.57 - Accepted - runtime 47ms - memory 12.6MB.py)
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

- Function signature: `def largestTriangleArea(self, points):`
- Return path: `return max(abs(`
- Loop step: `for a,b,c in combinations(points,3))`

## Note

This file is auto-generated from your currently accepted submission code.
