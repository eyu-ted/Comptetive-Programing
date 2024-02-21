class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        end=0
        ans=[]
        l=0
        for i,n in enumerate(s):
            dic[n]=i
        for i,n in enumerate(s):
            end=max(end,dic[n])
            l+=1
            if i ==end:
                ans.append(l)
                l=0
        return ans

             
        