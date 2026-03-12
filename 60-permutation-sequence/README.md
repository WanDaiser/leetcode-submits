# 60. Permutation Sequence

- Problem statement: [`60-permutation-sequence.md`](./60-permutation-sequence.md)
- Referenced submission: [`2025-11-16 17.11.24 - Accepted - runtime 0ms - memory 12.4MB.py`](./2025-11-16 17.11.24 - Accepted - runtime 0ms - memory 12.4MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(n)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(n)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Hash-table based lookup
- Stack usage
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def getPermutation(self, n, k):`
- Loop step: `for i in range(1, n + 1):`
- Loop step: `for i in range(n, 0, -1):`
- Data-structure operation: `ans.append(nums.pop(index))`
- Return path: `return ''.join(ans)`

## Note

This file is auto-generated from your currently accepted submission code.
