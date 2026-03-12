# 1528. Kids With The Greatest Number Of Candies

- Problem statement: [`1528-kids-with-the-greatest-number-of-candies.md`](./1528-kids-with-the-greatest-number-of-candies.md)
- Referenced submission: [`2025-10-15 22.36.40 - Accepted - runtime 0ms - memory 17.7MB.py`](./2025-10-15 22.36.40 - Accepted - runtime 0ms - memory 17.7MB.py)
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

- Function signature: `def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:`
- Loop step: `for i in range(len(candies)):`
- Data-structure operation: `ans.append(candies[i]+extraCandies>=max(candies))`
- Return path: `return ans`

## Note

This file is auto-generated from your currently accepted submission code.
