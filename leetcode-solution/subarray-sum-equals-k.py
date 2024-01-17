class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans=0
        dic={0:1}
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            dif = total-k
            if dif in dic:
                ans+=dic[dif]
            dic[total]=1+dic.get(total,0)
        return ans
