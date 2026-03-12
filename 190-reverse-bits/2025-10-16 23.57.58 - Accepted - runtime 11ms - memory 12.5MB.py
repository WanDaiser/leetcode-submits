class Solution(object):
    def reverseBits(self, n):
        n=bin(n)[2:]
        n=list(n)
        n.reverse()
        m="".join(n)
        while len(m)<32:
            m+="0"

        return int(m,2)
        