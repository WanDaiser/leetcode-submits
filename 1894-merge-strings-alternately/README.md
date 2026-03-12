# 1894. Merge Strings Alternately

- Problem statement: [`1894-merge-strings-alternately.md`](./1894-merge-strings-alternately.md)
- Referenced submission: [`2025-10-15 22.13.30 - Accepted - runtime 7ms - memory 12.4MB.py`](./2025-10-15 22.13.30 - Accepted - runtime 7ms - memory 12.4MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(n)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(n)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def mergeAlternately(self, word1, word2):`
- Loop step: `while i < len(word1) or i < len(word2):`
- Conditional check: `if i < len(word1):`
- Data-structure operation: `result.append(word1[i])`
- Conditional check: `if i < len(word2):`
- Data-structure operation: `result.append(word2[i])`
- Return path: `return "".join(result)`

## Note

This file is auto-generated from your currently accepted submission code.
