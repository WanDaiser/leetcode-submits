class Solution(object):
    def findMinDifference(self, tp):
        minutes=[]
        for t in tp:
            h,m=map(int,t.split(":"))
            minutes.append(h*60+m)
        minutes.sort() 
        min_fark=1440
        for i in range(1,len(minutes)):
            fark=minutes[i]-minutes[i-1]
            min_fark=min(min_fark,fark)
        son_fark=1440-(minutes[-1]-minutes[0])
        min_fark=min(min_fark,son_fark)
        return min_fark

