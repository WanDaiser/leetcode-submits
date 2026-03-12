class Solution(object):
    def numberOfSteps(self, num):
        a=0
        while num!=0:
            if num%2==0:
                num/=2
            elif num%2==1:
                num-=1
            a+=1
        return a 
        