class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic={0:1}
        total=0
        ans=0
        for i in range(len(nums)):
            total+=nums[i]
            r=total%k
            if r in dic:
                ans+=dic[r]
            dic[r]=1+dic.get(r,0)
        return ans

        