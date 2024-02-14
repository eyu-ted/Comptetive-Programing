class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=0
        maxx=float("-inf")
        for i in range(len(nums)):
            currsum+=nums[i]
            maxx=max(maxx,currsum)
            if currsum<0:
                currsum=0     
        return maxx
            
        