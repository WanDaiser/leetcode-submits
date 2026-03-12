class Solution(object):
    def jump(self, nums):
        dp={}
        j=0
        end=0
        uz=0
        for i in range(len(nums)-1):
            uz =max(uz,i+nums[i])
            if i ==end:
                j+=1
                end=uz
        return j

        