class Solution:
    def maxScore(self, s: str) -> int:
        rightsum=s.count("1")
        if s[0]=="1":
            rightsum-=1
        leftsum=0
        maxx=float("-inf")
        for i in range(len(s)):
            total=rightsum+leftsum
            maxx=max(total,maxx)
            if s[i]=="0":
                leftsum+=1
            elif i!=0 and s[i]=="1":
                rightsum-=1
            
        return maxx
            
                