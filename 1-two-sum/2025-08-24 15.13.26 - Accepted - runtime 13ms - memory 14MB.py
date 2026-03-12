class Solution(object):
    def twoSum(self, nums, target):
        num_to_index = {}  # sayıyı -> indeksi tutacak
        
        nums_with_index = list(enumerate(nums))
        nums_with_index.sort(key=lambda x: x[1])

        left, right = 0, len(nums)-1
        while left < right:
            total = nums_with_index[left][1] + nums_with_index[right][1]
            if total == target:
                return [nums_with_index[left][0], nums_with_index[right][0]]
            elif total < target:
                left += 1
            else:
                right -= 1

