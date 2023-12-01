class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dic={}
        ans=0
        for i in range(len(nums)):
            if nums[i] in dic:
                ans+=dic[nums[i]]
                dic[nums[i]]+= 1
            else:
                dic[nums[i]]=1
        return ans

            
        