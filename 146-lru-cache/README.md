# 146. Lru Cache

- Problem statement: [`146-lru-cache.md`](./146-lru-cache.md)
- Referenced submission: [`2025-11-17 15.29.06 - Accepted - runtime 279ms - memory 78.6MB.py`](./2025-11-17 15.29.06 - Accepted - runtime 279ms - memory 78.6MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Dynamic programming / memoization

## Step-by-Step Code Walkthrough

- Function signature: `def __init__(self, key, value):`
- Function signature: `def __init__(self, capacity):`
- Function signature: `def _remove(self, node):`
- Function signature: `def _add_to_front(self, node):`
- Function signature: `def get(self, key):`
- Conditional check: `if key not in self.cache:`
- Return path: `return -1`
- Return path: `return node.value`

## Note

This file is auto-generated from your currently accepted submission code.
