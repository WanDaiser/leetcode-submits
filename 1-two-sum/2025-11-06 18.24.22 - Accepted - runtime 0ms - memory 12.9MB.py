class Solution(object):
    def twoSum(self, nums, target):
        goruldu={}
        for i ,num in enumerate(nums):
            diff =target-num           
            if diff in goruldu:
                return [goruldu[diff],i]
            goruldu[num]=i
            
        