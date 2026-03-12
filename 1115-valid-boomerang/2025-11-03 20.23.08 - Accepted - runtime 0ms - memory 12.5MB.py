class Solution(object):
    def isBoomerang(self, p):
        if p[0] == p[1] or p[1] == p[2] or p[0] == p[2]:
            return False
        return (p[1][1] - p[0][1]) * (p[2][0] - p[1][0]) != (p[2][1] - p[1][1]) * (p[1][0] - p[0][0])
