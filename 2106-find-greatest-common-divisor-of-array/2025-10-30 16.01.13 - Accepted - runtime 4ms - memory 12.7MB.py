import fractions

class Solution(object):
    def findGCD(self, nums):
        a, b = min(nums), max(nums)
        return fractions.gcd(a, b)