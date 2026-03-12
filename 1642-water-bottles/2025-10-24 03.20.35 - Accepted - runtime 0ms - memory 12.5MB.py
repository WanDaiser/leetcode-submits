class Solution(object):
    def numWaterBottles(self, nb, ne):
        icilensise = nb 
        bos = nb         

        while bos >= ne:
            yeni = bos // ne 
            icilensise += yeni    
            bos = bos % ne + yeni 
        return icilensise
