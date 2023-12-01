class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        maxx=max(len(word2),len(word1))
        for i in range(maxx):
            if i<len(word1):
                res+=word1[i]
            if i<len(word2):
                res+=word2[i]
        return res
