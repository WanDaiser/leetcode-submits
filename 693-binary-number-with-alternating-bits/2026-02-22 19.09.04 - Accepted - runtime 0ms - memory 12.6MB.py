class Solution(object):
    def hasAlternatingBits(self, n):
            b=bin(n)[2:]
            for i in range(1,len(b)):
                if b[i]==b[i-1]:
                    return False
            return True
        