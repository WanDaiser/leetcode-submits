class Solution(object):
    def minimumOperations(self, nums):
        return sum(1 for n in nums if n% 3)
            
        

        