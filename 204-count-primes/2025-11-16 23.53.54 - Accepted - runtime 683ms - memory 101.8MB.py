class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        import math
        limit = int(math.sqrt(n))
        for i in range(2, limit + 1):
            if sieve[i]:
                step = i
                start = i * i
                sieve[start:n:step] = [False] * ((n - start - 1)//step + 1)
        return sum(sieve)

        