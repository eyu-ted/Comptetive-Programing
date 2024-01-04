class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=float("inf")
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while r>l:
                s=nums[i]+nums[l]+nums[r]
                if abs(s-target)<abs(ans-target):
                    ans=s
                if s<target:
                    l+=1
                elif s>target:
                    r-=1
                else:
                    return ans
        return ans



        