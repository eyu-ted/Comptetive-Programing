class Solution:
    def printVertically(self, s: str) -> List[str]:
        lis=s.split()
        m=0
        for ch in lis:
            if len(ch)>m:
                m=len(ch)


        ans=[""]*m
        for i in range(m):
            for j in range(len(lis)):
                if i>=len(lis[j]):
                    ans[i]+=" "
                else:
                    ans[i]+=lis[j][i]
            ans[i] = ans[i].rstrip()
        return ans

                
