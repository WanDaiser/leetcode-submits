class Solution(object):
    def reverse(self, x):
        xlist=list(str(x))
        finalresult=[]
        if xlist[0]=="-":
            finalresult.append("-")
            xlist.pop(0)
        finalresult+=reversed(xlist)
        res = int(''.join(finalresult))
        if res<-2147483648 or res>2147483647:
            return 0
        return res