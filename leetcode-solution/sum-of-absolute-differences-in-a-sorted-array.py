class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        rightotal=0
        for n in nums:
            rightotal+=n
        leftotal=0
        for i,n in enumerate(nums):
            rightsum=rightotal-n*(len(nums)-i)
            rightotal-=n
            leftsum=n*i-leftotal
            leftotal+=n
            nums[i]=leftsum+rightsum
        return nums

        