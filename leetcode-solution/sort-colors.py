class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            while i>0 and nums[i]<nums[i-1]:
                temp=nums[i]
                nums[i]=nums[i-1]
                nums[i-1]=temp
                i-=1
        return nums