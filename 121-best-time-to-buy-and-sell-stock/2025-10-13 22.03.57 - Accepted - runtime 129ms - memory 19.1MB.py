class Solution(object):
    def maxProfit(self, prices):
        minp=float('inf')
        maxp=0
        for price in prices:
            minp=min(minp,price)
            maxp=(max(maxp,price-minp))
        return maxp
        