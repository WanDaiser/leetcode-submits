class Solution:
    def reverse(self, x):        
        MIN_INT = -(2**31)
        MAX_INT = 2**31 - 1
        reversed_num = 0 
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:      
            pop = x % 10
            reversed_num = reversed_num * 10 + pop    
            x //= 10  
        reversed_num *= sign
        if reversed_num < MIN_INT or reversed_num > MAX_INT:
            return 0       
        return reversed_num