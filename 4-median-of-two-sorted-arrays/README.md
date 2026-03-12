# 4. Median Of Two Sorted Arrays

- Problem statement: [`4-median-of-two-sorted-arrays.md`](./4-median-of-two-sorted-arrays.md)
- Referenced submission: [`2025-11-06 18.42.45 - Accepted - runtime 5ms - memory 12.7MB.py`](./2025-11-06 18.42.45 - Accepted - runtime 5ms - memory 12.7MB.py)
- Language: **Python**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n%20log%20n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(n log n)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Sorting-based approach

## Step-by-Step Code Walkthrough

- Function signature: `def findMedianSortedArrays(self, nums1, nums2):`
- Conditional check: `if len(nums3)%2==1:`
- Return path: `return nums3[int(len(nums3)/2)]`
- Conditional check: `elif len(nums3)%2==0:`
- Return path: `return (nums3[(len(nums3)//2)-1]+nums3[(len(nums3)//2)])/2.0`

## Note

This file is auto-generated from your currently accepted submission code.
