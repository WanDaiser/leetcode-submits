class Solution(object):
    def repeatedNTimes(self, nums):
        dict={}
        for i in nums:
            if i in dict:
                return i
            else:
                dict[i]=i
            
        