class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxxcounter=0
        maxx=0
        l=0
        dic={}
        for r in range(len(s)):
            dic[s[r]]=1+dic.get(s[r],0)
            maxxcounter=max(maxxcounter,dic[s[r]])
            while r-l+1 -maxxcounter >k:
                dic[s[l]]-=1
                l+=1
               
            maxx= max(maxx,r-l+1)
        return maxx
        