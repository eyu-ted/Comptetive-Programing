class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortcopy=sorted(heights)
        ans=0
        for i in range(len(heights)):
            if sortcopy[i]!=heights[i]:
                ans+=1
        return ans
        