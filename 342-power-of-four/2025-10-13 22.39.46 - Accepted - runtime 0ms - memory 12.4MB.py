class Solution(object):
    def isPowerOfFour(self, n):
        return (True if n>0 and ( n & (n-1)) == 0 and n%3==1 else False)
        