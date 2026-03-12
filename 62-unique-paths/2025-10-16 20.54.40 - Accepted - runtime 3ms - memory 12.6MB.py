class Solution(object):
    def uniquePaths(self, m, n):
        dp={(0,0):0,(1,0):1,(0,1):1}
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    dp[(i,j)]=1
                else:
                    dp[(i,j)]=dp[(i-1,j)] + dp[(i,j-1)]
                
        return dp[(m-1,n-1)]