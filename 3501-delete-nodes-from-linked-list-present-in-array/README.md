# 3501. Delete Nodes From Linked List Present In Array

- Problem statement: [`3501-delete-nodes-from-linked-list-present-in-array.md`](./3501-delete-nodes-from-linked-list-present-in-array.md)
- Referenced submission: [`2025-11-09 23.47.22 - Accepted - runtime 124ms - memory 98.7MB.py`](./2025-11-09 23.47.22 - Accepted - runtime 124ms - memory 98.7MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(n)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(n)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def modifiedList(self, nums, head):`
- Data-structure operation: `delete_set = set(nums)`
- Loop step: `while curr:`
- Conditional check: `if curr.val in delete_set:`
- Conditional check: `else:`
- Return path: `return dummy.next`

## Note

This file is auto-generated from your currently accepted submission code.
