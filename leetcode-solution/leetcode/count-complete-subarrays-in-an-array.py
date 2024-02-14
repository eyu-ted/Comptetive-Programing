class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        sett=set(nums)
        l=0
        ans=0
        for r in range(len(nums)):
            dic[nums[r]]+=1
            while len(dic)==len(sett):
                ans+=len(nums)-r
                dic[nums[l]]-=1
                if dic[nums[l]]==0:
                    dic.pop(nums[l])
                l+=1
            
        return ans

           
             