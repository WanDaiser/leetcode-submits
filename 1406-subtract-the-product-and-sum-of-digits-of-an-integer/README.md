# 1406. Subtract The Product And Sum Of Digits Of An Integer

- Problem statement: [`1406-subtract-the-product-and-sum-of-digits-of-an-integer.md`](./1406-subtract-the-product-and-sum-of-digits-of-an-integer.md)
- Referenced submission: [`2025-11-03 20.43.37 - Accepted - runtime 0ms - memory 17.5MB.py`](./2025-11-03 20.43.37 - Accepted - runtime 0ms - memory 17.5MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def subtractProductAndSum(self, n: int) -> int:`
- Return path: `return math.prod(int(d) for d in str(n)) - sum(int(d) for d in str(n))`

## Note

This file is auto-generated from your currently accepted submission code.
