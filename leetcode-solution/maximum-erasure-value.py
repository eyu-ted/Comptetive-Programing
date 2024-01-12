class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        l=0
        total=0
        maxx=float("-inf")
        for r in range(len(nums)):
            total+=nums[r]
            dic[nums[r]]+=1
            while dic[nums[r]] >1:
                dic[nums[l]]-=1
                total-=nums[l]
                l+=1
            maxx=max(maxx,total)
        return maxx

        