class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dicn={}
        for i,n in enumerate(nums):
            diff=target-n
            if n in dicn:
                return [dicn[n],i]
            else:
                dicn[diff]=i

        