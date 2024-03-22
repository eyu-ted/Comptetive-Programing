class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            num = abs(nums[i])

            if nums[num-1]>0:
                nums[num-1] *=-1
            else:
                ans.append(num)
        return ans