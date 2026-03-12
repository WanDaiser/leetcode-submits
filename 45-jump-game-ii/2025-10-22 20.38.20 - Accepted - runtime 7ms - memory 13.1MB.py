class Solution(object):
    def jump(self, n):
        j=0
        e=0
        u=0
        for i in range(len(n)-1):
            u=max(u,i+n[i])
            if i==e:
                j+=1
                e=u
        return j

        