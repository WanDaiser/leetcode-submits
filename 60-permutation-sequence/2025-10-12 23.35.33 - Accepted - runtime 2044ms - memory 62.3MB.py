import itertools
class Solution(object):
    def getPermutation(self, n, k):
        numtoN=[]
        for i in range(1,n+1):
            numtoN.append(str(i))
        n=list(itertools.permutations(numtoN))
        result=''.join(n[k-1])
        return result
        