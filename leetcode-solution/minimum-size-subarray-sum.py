class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minn=float("inf")
        l=0
        currsum=0
        for r in range(len(nums)):
            currsum+=nums[r]
            while currsum>=target:
                minn=min(minn,r-l+1)
                currsum-=nums[l]
                l+=1
        return 0 if minn==float("inf") else minn

        