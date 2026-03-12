# 118. Pascals Triangle

- Problem statement: [`118-pascals-triangle.md`](./118-pascals-triangle.md)
- Referenced submission: [`2025-11-16 17.15.42 - Accepted - runtime 0ms - memory 12.6MB.py`](./2025-11-16 17.15.42 - Accepted - runtime 0ms - memory 12.6MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def generate(self, numRows):`
- Conditional check: `if numRows==1:`
- Return path: `return [[1]]`
- Loop step: `for i in range(numRows-2):`
- Data-structure operation: `currlist.append(1)`
- Loop step: `for j in range(0,len(prevlist)-1):`
- Data-structure operation: `currlist.append(prevlist[j]+prevlist[j+1])`
- Data-structure operation: `currlist.append(1)`

## Note

This file is auto-generated from your currently accepted submission code.
