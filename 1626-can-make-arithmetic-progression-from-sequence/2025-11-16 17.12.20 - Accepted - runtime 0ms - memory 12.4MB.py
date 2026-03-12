class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        prev=arr[0]-arr[1]
        for i in range(len(arr)-1):
            if prev!=arr[i]-arr[i+1]:
                return False
        return True
        