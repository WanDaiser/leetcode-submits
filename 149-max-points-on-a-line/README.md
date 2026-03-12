# 149. Max Points On A Line

- Problem statement: [`149-max-points-on-a-line.md`](./149-max-points-on-a-line.md)
- Referenced submission: [`2026-02-22 18.39.22 - Accepted - runtime 43ms - memory 12.6MB.py`](./2026-02-22 18.39.22 - Accepted - runtime 43ms - memory 12.6MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Data-structure operation: `from collections import defaultdict`
- Function signature: `def gcd(a,b):`
- Loop step: `while b:`
- Return path: `return a`
- Function signature: `def maxPoints(self, points):`
- Conditional check: `if len(points) <= 2: return len(points)`
- Loop step: `for i, (x1, y1) in enumerate(points):`
- Data-structure operation: `slopes, dup = defaultdict(int), 1`

## Note

This file is auto-generated from your currently accepted submission code.
