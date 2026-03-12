class Solution(object):
    def divide(self, dividend, divisor):
        quotient = abs(dividend) // abs(divisor)
        if (dividend < 0) != (divisor < 0):
            quotient = -quotient
        return max(min(quotient, 2**31 - 1), -2**31)

        