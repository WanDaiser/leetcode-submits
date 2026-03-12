class Solution(object):
    def plusOne(self, digits):
        num = int("".join(map(str,digits)))
        l=[int(d)for d in str(num+1)]
        return l
            