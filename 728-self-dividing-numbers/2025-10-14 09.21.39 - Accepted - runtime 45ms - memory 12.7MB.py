class Solution(object):
    def selfDividingNumbers(self, left, right):
        n=left
        output=[]
        for i in range(left,right+1):
            if (len(str(n))==1):
                output.append(n)
            else:
                a=list(str(n))
                bolundumu=True
                for item in a:
                    if int(item)==0:
                        bolundumu=False
                    elif n%int(item)!=0:
                        bolundumu=False
                        break
                if bolundumu:
                    output.append(n)    

            n+=1
        return output
        