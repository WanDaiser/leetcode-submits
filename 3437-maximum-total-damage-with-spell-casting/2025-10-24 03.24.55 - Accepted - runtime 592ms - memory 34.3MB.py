from collections import Counter

class Solution(object):
    def maximumTotalDamage(self, power):
        count = Counter(power)
        unique = sorted(count.keys())
        n = len(unique)
        dp = [0] * n
        for i in range(n):
            curr_damage = unique[i] * count[unique[i]]
            j = i - 1
            while j >= 0 and unique[j] >= unique[i] - 2:
                j -= 1
            if j >= 0:
                dp[i] = max(dp[i-1], curr_damage + dp[j])
            else:
                dp[i] = max(dp[i-1], curr_damage)
        return dp[-1]