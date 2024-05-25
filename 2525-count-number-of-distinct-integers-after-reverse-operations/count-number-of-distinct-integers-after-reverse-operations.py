class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rev= set(nums)
        for num in nums:
            rev.add(int(str(num)[::-1]))

        return len(set(rev))