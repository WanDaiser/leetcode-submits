class Solution(object):
    def convert(self, s, nr):
        if nr==1 or nr>=len(s):
            return s
        rows=[""]*nr
        anlik=0
        asagi=False
        for c in s:
            rows[anlik]+=c
            if anlik ==0 or anlik==nr-1:
                asagi=not asagi
            if asagi:
                anlik+=1
            else:
                anlik-=1
        return "".join(rows)