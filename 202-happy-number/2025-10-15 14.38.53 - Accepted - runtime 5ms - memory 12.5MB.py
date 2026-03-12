class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            a = list(str(n))
            n = 0
            for digit in a:
                n += int(digit) ** 2
        return True
        