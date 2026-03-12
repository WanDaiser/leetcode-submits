class Solution(object):
    def maxArea(self, height):
        if not height or len(height)<2:
            return 0
        l=0
        r=len(height)-1
        maxa=0
        while l<r:
            width=r-l
            area=min(height[l],height[r])*width
            maxa= max(maxa,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxa
        