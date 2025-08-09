class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l = 0 
        summ = 0
        ans = float("inf")
        for r in range(len(nums)):
            
            summ += nums[r]
            while l<=r and summ >= target:
                summ -= nums[l]
                ans = min(ans, r-l+1)
                l+=1
                
        
        return ans if ans!=float("inf") else 0


            