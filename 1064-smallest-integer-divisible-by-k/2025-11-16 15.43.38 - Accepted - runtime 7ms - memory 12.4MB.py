class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k % 2 == 0 or k % 5 == 0:
            return -1

        curr = 0
        length = 0

        while True:
            curr = (curr * 10 + 1) % k
            length += 1
            if curr == 0:
                return length

        