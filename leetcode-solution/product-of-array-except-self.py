class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftproduct=1
        rightproduct=1
        ans=[0]*len(nums)

        for i in range(len(nums)):
            ans[i]=leftproduct
            leftproduct*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            ans[i]=ans[i]*rightproduct
            rightproduct*=nums[i]
        return ans
        
        