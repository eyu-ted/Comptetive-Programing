class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        lis=[]
        ans=0
        for col in range(len(strs[0])):
            for row in range(len(strs)):
                lis.append(strs[row][col])
            if lis!=sorted(lis):
                ans+=1
            lis=[]
        return ans

                
        