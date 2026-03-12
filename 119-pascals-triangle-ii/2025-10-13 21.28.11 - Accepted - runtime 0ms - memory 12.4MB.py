class Solution(object):
    def getRow(self, numRows):
        numRows+=1
        if numRows==0:
            return [1]
        sonuclistesi=[[1],[1,1]]
        prevlist=[1,1]
        currlist=[]
        for i in range(numRows-2):
            currlist.append(1)
            for j in range(0,len(prevlist)-1):
                currlist.append(prevlist[j]+prevlist[j+1])
            currlist.append(1)
            sonuclistesi.append(currlist)
            prevlist=currlist
            currlist=[]
        return sonuclistesi[numRows-1]


                

        
        