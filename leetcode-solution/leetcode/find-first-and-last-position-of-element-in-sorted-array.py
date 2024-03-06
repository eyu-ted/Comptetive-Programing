class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        ans = [-1,-1]
        l=0
        r=len(nums)-1
        while l<=r:

            mid = (l+r)//2

            if nums[mid] == target:
                ans[0] = mid
                r = mid-1
            elif nums[mid] >  target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
        l=0
        r=len(nums)-1
        while l<=r:

            mid = (l+r)//2

            if nums[mid] == target:
                ans[1] = mid
                l = mid+1
            elif nums[mid] >  target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
        return ans

        