class Solution:
    def minimumSteps(self, s: str) -> int:
        
        r=len(s)-1
        ansl=0
        for l in range(len(s)-1,-1,-1):
            if s[l]=="1":
                ansl+=r-l
                r-=1
        return ansl


        