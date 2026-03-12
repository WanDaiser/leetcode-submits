# 345. Reverse Vowels Of A String

- Problem statement: [`345-reverse-vowels-of-a-string.md`](./345-reverse-vowels-of-a-string.md)
- Referenced submission: [`2025-10-16 08.13.00 - Accepted - runtime 7ms - memory 18.6MB.py`](./2025-10-16 08.13.00 - Accepted - runtime 7ms - memory 18.6MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(n)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(n)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Hash-table based lookup
- Two-pointer style traversal
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def reverseVowels(self, s: str) -> str:`
- Data-structure operation: `vowels = set("aeiouAEIOU")`
- Loop step: `while left < right:`
- Conditional check: `if s[left] not in vowels:`
- Conditional check: `if s[right] not in vowels:`
- Return path: `return "".join(s)`

## Note

This file is auto-generated from your currently accepted submission code.
