class Solution(object):
    def checkStraightLine(self, c):
        return all((c[i+1][1]-c[i][1])*(c[i+2][0]-c[i+1][0]) == (c[i+2][1]-c[i+1][1])*(c[i+1][0]-c[i][0]) for i in range(len(c)-2))
