class Solution(object):
    def countDigitOne(self, n):
        c=0
        digit=1
        while n// digit>0:
            h = n//(digit*10)
            cur=(n//digit)%10
            low =n%digit
            if cur==0:
                c+=h*digit
            elif cur==1:
                c+=h*digit+low+1
            else:
                c+=(h+1)*digit
            digit*=10
        return c
        