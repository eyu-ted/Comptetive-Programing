class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1]*len(nums)
        stack=[]

        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                ans[stack[-1]]=nums[i]
                stack.pop()

            stack.append(i)

        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                ans[stack[-1]]=nums[i]
                stack.pop()
            if not stack:
                break
        return ans
        