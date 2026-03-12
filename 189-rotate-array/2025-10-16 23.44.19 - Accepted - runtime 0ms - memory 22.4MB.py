class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        ans = nums[-k:] + nums[:-k]
        nums[:] = ans 
        

        