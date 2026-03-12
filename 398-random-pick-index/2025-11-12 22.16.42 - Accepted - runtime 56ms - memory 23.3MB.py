import random
from collections import defaultdict

class Solution(object):
    def __init__(self, nums):
        self.positions = defaultdict(list)
        for i, num in enumerate(nums):
            self.positions[num].append(i)

    def pick(self, target):
        return random.choice(self.positions[target])
