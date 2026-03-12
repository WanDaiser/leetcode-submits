class Solution(object):
    def countOperations(self, num1, num2):
        op=0
        while(num1!=0 and num2!=0):
            if num1 >= num2:
                num1-=num2
                op+=1
            else:
                num2-=num1
                op+=1
        return op
        