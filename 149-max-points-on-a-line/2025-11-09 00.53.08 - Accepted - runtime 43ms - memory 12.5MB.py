from collections import defaultdict
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2: return len(points)
        res = 0
        for i, (x1, y1) in enumerate(points):
            slopes, dup = defaultdict(int), 1
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1
                if dx == dy == 0:
                    dup += 1
                    continue
                g = gcd(dy, dx)
                slopes[(dy//g if g else dy, dx//g if g else dx)] += 1
            res = max(res, dup + (max(slopes.values()) if slopes else 0))
        return res