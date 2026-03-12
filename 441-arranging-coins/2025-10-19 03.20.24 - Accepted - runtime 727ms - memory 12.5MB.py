class Solution(object):
    def arrangeCoins(self, n):
        if n==1 or n==2:
            return 1
        elif n==3:
            return 2
        a=1
        while a<n:
            if (((a+1)*a)/2)>n:
                return a-1
            a+=1
        