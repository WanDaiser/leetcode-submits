class Solution(object):
    def addToArrayForm(self, num, k):
        a=int("".join(map(str,num)))
        a+=k
        ans=[int(s) for s in str(a)]
        return ans
        