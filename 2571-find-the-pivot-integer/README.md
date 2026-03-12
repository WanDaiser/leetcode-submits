# 2571. Find The Pivot Integer

- Problem statement: [`2571-find-the-pivot-integer.md`](./2571-find-the-pivot-integer.md)
- Referenced submission: [`2025-11-16 17.12.26 - Accepted - runtime 13ms - memory 12.4MB.py`](./2025-11-16 17.12.26 - Accepted - runtime 13ms - memory 12.4MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def pivotInteger(self, n):`
- Loop step: `for i in range(n+1):`
- Conditional check: `if (i*(i+1))/2 == (((n-i+1)*(i+n))/2):`
- Return path: `return pivot`

## Note

This file is auto-generated from your currently accepted submission code.
