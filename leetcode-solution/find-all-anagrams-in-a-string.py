class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdic={}
        for n in p:
            pdic[n]=1+pdic.get(n,0)
        adic={}
        l=0
        ans=[]
        for i in range(len(s)):
            adic[s[i]]=1+adic.get(s[i],0)
            if adic==pdic:
                ans.append(l)
            if i+1>=len(p):
                adic[s[l]]-=1
                if adic[s[l]]==0:
                    adic.pop(s[l])
                l+=1
        return ans


            

        