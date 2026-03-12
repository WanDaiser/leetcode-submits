class Solution(object):
    def selfDividingNumbers(self, left, right):
        ans = []
        def selfdiv(a):
            for ch in str(a):
                d = int(ch)
                if d == 0 or a % d != 0:
                    return False
            return True
        for i in range(left, right + 1):
            if selfdiv(i):
                ans.append(i)
        return ans
