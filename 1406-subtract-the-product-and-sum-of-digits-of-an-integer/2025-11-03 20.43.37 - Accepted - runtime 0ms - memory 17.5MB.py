class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return math.prod(int(d) for d in str(n)) - sum(int(d) for d in str(n))
