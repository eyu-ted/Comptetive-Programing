class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic={n[0]:0 for i,n in enumerate(matches)}
        ans=[[],[]]

        for n in matches:
            dic[n[1]]=dic.get(n[1],0)+1
        for key,value in dic.items():
            if value==1:
                ans[1].append(key)
            elif value==0 :
                ans[0].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans

        
        