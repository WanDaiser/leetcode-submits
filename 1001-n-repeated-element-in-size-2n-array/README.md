# 1001. N Repeated Element In Size 2N Array

- Problem statement: [`1001-n-repeated-element-in-size-2n-array.md`](./1001-n-repeated-element-in-size-2n-array.md)
- Referenced submission: [`2026-01-02 01.19.42 - Accepted - runtime 0ms - memory 13.3MB.py`](./2026-01-02 01.19.42 - Accepted - runtime 0ms - memory 13.3MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def repeatedNTimes(self, nums):`
- Data-structure operation: `dict={}`
- Loop step: `for i in nums:`
- Conditional check: `if i in dict:`
- Return path: `return i`
- Conditional check: `else:`
- Data-structure operation: `dict[i]=i`

## Note

This file is auto-generated from your currently accepted submission code.
