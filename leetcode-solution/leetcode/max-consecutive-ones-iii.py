class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        c=0
        maxx=0
        for r in range(len(nums)):
            if nums[r]==0:
                c+=1
            if c>k:
                if nums[l]==0:
                    c-=1
                l+=1
            if c<=k:
                maxx=max(maxx,r-l+1)

        return maxx
        