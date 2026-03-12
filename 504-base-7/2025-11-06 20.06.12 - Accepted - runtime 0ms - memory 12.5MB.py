class Solution(object):
    def convertToBase7(self, num):
        if num <0:
            return "-"+self.convertToBase7(-num)
        return str(num) if -7 < num < 7 else self.convertToBase7(num//7)+str(num%7)
        