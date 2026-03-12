class Solution(object):
    def getPermutation(self, n, k):
        k -= 1
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i
        nums = [str(i) for i in range(1, n+1)]
        ans = []
        for i in range(n, 0, -1):
            block_size = fact[i-1]
            index = k // block_size
            k %= block_size
            ans.append(nums.pop(index))
        return ''.join(ans)
