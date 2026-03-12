class Solution(object):
    def addToArrayForm(self, num, k):
        a=int("".join(map(str,num)))+k
        return [int(s) for s in str(a)]

        