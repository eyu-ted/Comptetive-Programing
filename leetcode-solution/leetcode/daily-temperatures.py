class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i,n in enumerate(temperatures):
            while stack and n>stack[-1][1]:
                indx,temp=stack.pop()
                ans[indx]=i-indx
            stack.append([i,n])
        return ans