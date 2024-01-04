class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>=1 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while r>l:
                total=nums[i]+nums[l]+nums[r]
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while r>l and nums[l]==nums[l-1]:
                        l+=1
                    r-=1
                    while r>l and nums[r]==nums[r+1]:
                        r-=1
        return ans
        