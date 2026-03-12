from itertools import combinations
class Solution(object):
    def largestTriangleArea(self, points):
        return max(abs(
            a[0]*(b[1]-c[1])+
            b[0]*(c[1]-a[1])+
            c[0]*(a[1]-b[1])
        )*0.5
        for a,b,c in combinations(points,3))
        