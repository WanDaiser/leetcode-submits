class Solution(object):
    def isPalindrome(self, x):
        if x > 0:
            rev_x = int(str(x)[::-1])
            if x==rev_x:
                return True
            else:
                return False
        elif len(str(x)) < 2:
            return True        
        else:
            return False            