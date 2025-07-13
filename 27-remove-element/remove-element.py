class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums)-1
        k = len(nums) - nums.count(val)
        for left in range(len(nums)):
            if nums[left] == val:
                
                while right>=0 and right > left and nums[right] == val:
                    right-=1
                nums[left], nums[right] = nums[right] , nums[left]
        return k