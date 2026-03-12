class Solution(object):
    def moveZeroes(self, nums):
        i=0
        zeros=0
        if len(nums)!=1:         
            while i<len(nums):
                if nums[i]==0:
                    nums.pop(i)
                    zeros+=1
                else:
                    i+=1
        nums+=[0]*zeros