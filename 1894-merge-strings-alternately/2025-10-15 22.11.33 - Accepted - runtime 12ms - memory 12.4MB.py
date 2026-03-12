class Solution(object):
    def mergeAlternately(self, word1, word2):
        a=""
        for i in range(min(len(word1),len(word2))):
            a+=word1[i]
            a+=word2[i]
        if len(word1)==len(word2):
            return a
        elif len(word1)>len(word2):
            for i in range(len(word2),len(word1)):
                a+=word1[i]
            return a
        else:
            for i in range(len(word1),len(word2)):
                a+=word2[i]
            return a