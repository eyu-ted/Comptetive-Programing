class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        tot = ans = nums[0]
        for i in range(1,len(nums)):
            tot += nums[i]
            ans=max( ans , math.ceil( tot / (i+1) ))
        return ans