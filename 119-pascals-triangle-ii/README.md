# 119. Pascals Triangle Ii

- Problem statement: [`119-pascals-triangle-ii.md`](./119-pascals-triangle-ii.md)
- Referenced submission: [`2025-10-13 21.28.11 - Accepted - runtime 0ms - memory 12.4MB.py`](./2025-10-13 21.28.11 - Accepted - runtime 0ms - memory 12.4MB.py)
- Language: **Python**

## Approach

- Hash-table based lookup
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `def getRow(self, numRows):`
- Conditional check: `if numRows==0:`
- Return path: `return [1]`
- Loop step: `for i in range(numRows-2):`
- Data-structure operation: `currlist.append(1)`
- Loop step: `for j in range(0,len(prevlist)-1):`
- Data-structure operation: `currlist.append(prevlist[j]+prevlist[j+1])`
- Data-structure operation: `currlist.append(1)`

## Note

This file is auto-generated from your currently accepted submission code.
