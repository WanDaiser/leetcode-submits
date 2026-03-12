import random

class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        indices = [i for i, val in enumerate(self.nums) if val == target]
        return random.choice(indices)