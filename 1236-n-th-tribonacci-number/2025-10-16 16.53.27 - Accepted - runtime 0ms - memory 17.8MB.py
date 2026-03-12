class Solution:
    def tribonacci(self, n: int) -> int:
        x=0
        y=1
        z=1
        for i in range(n):
            x,y,z=y,z,x+y+z
        return x