# 398. Random Pick Index

- Problem statement: [`398-random-pick-index.md`](./398-random-pick-index.md)
- Referenced submission: [`2025-11-12 22.16.42 - Accepted - runtime 56ms - memory 23.3MB.py`](./2025-11-12 22.16.42 - Accepted - runtime 56ms - memory 23.3MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Data-structure operation: `from collections import defaultdict`
- Function signature: `def __init__(self, nums):`
- Data-structure operation: `self.positions = defaultdict(list)`
- Loop step: `for i, num in enumerate(nums):`
- Data-structure operation: `self.positions[num].append(i)`
- Function signature: `def pick(self, target):`
- Return path: `return random.choice(self.positions[target])`

## Note

This file is auto-generated from your currently accepted submission code.
