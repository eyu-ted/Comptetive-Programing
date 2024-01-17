class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        rightsum=sum(nums)
        leftsum=0
        for i in range(len(nums)):
            rightsum-=nums[i]
            if rightsum==leftsum:
                return i
            leftsum+=nums[i]
        return -1


        