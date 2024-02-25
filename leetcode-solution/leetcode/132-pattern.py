class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        minn=nums[0]
        for n in nums[1:]:
            while stack and stack[-1][0]<=n:
                stack.pop()
            if stack and n>stack[-1][1]:
                return True
            stack.append([n,minn])
            minn=min(minn,n)
        return  False

        
        