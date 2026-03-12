# 1626. Can Make Arithmetic Progression From Sequence

- Problem statement: [`1626-can-make-arithmetic-progression-from-sequence.md`](./1626-can-make-arithmetic-progression-from-sequence.md)
- Referenced submission: [`2025-11-16 17.12.34 - Accepted - runtime 0ms - memory 12.4MB.py`](./2025-11-16 17.12.34 - Accepted - runtime 0ms - memory 12.4MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Sorting-based approach
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def canMakeArithmeticProgression(self, arr):`
- Loop step: `for i in range(len(arr)-1):`
- Conditional check: `if prev!=arr[i]-arr[i+1]:`
- Return path: `return False`
- Return path: `return True`

## Note

This file is auto-generated from your currently accepted submission code.
