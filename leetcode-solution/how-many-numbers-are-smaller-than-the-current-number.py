class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d={}
        result = []

        for i in range(len(nums)):
            if temp[i] not in d:
                d[temp[i]]= i

        for i in range(len(nums)):
            result.append(d[nums[i]])

        return result