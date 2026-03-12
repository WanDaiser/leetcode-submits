class Solution(object):
    def isPalindrome(self, x):
        a=list(str(x))
        b=list(str(x))
        a.reverse()
        return a==b
    
        