class Solution(object):
    def pivotInteger(self, n):
        pivot=-1
        for i in range(n+1):
            if (i*(i+1))/2 == (((n-i+1)*(i+n))/2):
                pivot=i
        return pivot
