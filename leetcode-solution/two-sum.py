class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,n in enumerate(nums):
            diff=target-n
            if n in dic:
                return [dic[n],i]
            else:
                dic[diff]=i
