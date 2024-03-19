class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        ans =0
        nums.sort()

        for i in range(len(nums)):
            diff = target-nums[i]
            if diff >= nums[i]:
                index = bisect_right(nums,diff)
                l = index-i-1
                ans += 2**l

        return ans%((10**9)+7)
        