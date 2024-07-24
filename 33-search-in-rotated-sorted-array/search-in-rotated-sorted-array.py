class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l=0
        r= len(nums)-1
        while r>=l:
            midd = (l+r)//2

            if nums[midd] == target:
                return midd

            if nums[midd] >= nums[l]:

                if target> nums[midd] or target<nums[l]:
                    l=midd+1
                else:
                    r=midd-1
            else:

                if nums[midd]>target or target>nums[r]:
                    r=midd-1
                else:
                    l=midd+1
        

        return -1
