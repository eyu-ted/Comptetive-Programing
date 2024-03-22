class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        maxx = 0
        l=0
        count=0
        sett =set(word[0])
        for r in range(1,len(word)):
            if word[r]>=word[r-1]:
                sett.add(word[r])
            else:
                sett = set(word[r])
                l=r

            if len(sett) == 5:
                maxx = max(maxx,r-l+1)
        return maxx
