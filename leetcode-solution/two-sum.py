class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,n in enumerate(nums):
            d=target-n
            if d in dic:
                return [dic[d],i]
            dic[n]=i
        