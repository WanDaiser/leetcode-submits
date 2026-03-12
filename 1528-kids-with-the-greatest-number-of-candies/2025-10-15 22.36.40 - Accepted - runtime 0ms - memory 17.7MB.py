class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans =[]
        for i in range(len(candies)):
            ans.append(candies[i]+extraCandies>=max(candies))
        return ans