class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rev= []
        for num in nums:
            rev.append(int(str(num)[::-1]))
        nums.extend(rev)

        return len(set(nums))