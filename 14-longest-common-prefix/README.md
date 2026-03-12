# 14. Longest Common Prefix

- Problem statement: [`14-longest-common-prefix.md`](./14-longest-common-prefix.md)
- Referenced submission: [`2025-10-31 21.21.36 - Accepted - runtime 2ms - memory 12.5MB.py`](./2025-10-31 21.21.36 - Accepted - runtime 2ms - memory 12.5MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def longestCommonPrefix(self, strs):`
- Conditional check: `if not strs:`
- Return path: `return ""`
- Loop step: `for i in range(len(strs[0])):`
- Loop step: `for s in strs[1:]:`
- Conditional check: `if i == len(s) or s[i] != strs[0][i]:`
- Return path: `return strs[0][:i]`
- Return path: `return strs[0]`

## Note

This file is auto-generated from your currently accepted submission code.
