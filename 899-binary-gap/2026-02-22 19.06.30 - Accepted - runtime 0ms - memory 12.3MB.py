class Solution(object):
    def binaryGap(self, n):
        b=bin(n)[2:]
        max_gap=0
        last=-1
        for i,bit in enumerate(b):
            if bit=='1':
                if last!=-1:
                    max_gap=max(max_gap,i-last)
                last=i
        return max_gap