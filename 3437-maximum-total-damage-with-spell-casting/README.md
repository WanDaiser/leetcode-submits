# 3437. Maximum Total Damage With Spell Casting

- Problem statement: [`3437-maximum-total-damage-with-spell-casting.md`](./3437-maximum-total-damage-with-spell-casting.md)
- Referenced submission: [`2025-10-24 03.24.55 - Accepted - runtime 592ms - memory 34.3MB.py`](./2025-10-24 03.24.55 - Accepted - runtime 592ms - memory 34.3MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n%20log%20n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(n log n)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Hash-table based lookup
- Sorting-based approach
- Dynamic programming / memoization
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def maximumTotalDamage(self, power):`
- Loop step: `for i in range(n):`
- Loop step: `while j >= 0 and unique[j] >= unique[i] - 2:`
- Conditional check: `if j >= 0:`
- Conditional check: `else:`
- Return path: `return dp[-1]`

## Note

This file is auto-generated from your currently accepted submission code.
