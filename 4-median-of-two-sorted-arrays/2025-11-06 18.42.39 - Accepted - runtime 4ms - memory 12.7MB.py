class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums3=nums1+nums2
        nums3.sort()
        if len(nums3)%2==1:
            return nums3[int(len(nums3)/2)]
        elif len(nums3)%2==0:
            return (nums3[(len(nums3)//2)-1]+nums3[(len(nums3)//2)])/2.0
            