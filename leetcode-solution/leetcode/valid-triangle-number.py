class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        for i in range(len(nums)-1,-1,-1):
            l=0
            r=i-1
            while r>l:
                summ=nums[l]+nums[r]
                if summ>nums[i]:
                    ans+=r-l
                    r-=1
                elif summ<=nums[i]:
                    l+=1
        return ans
                    


        