class Solution:
    def maxScore(self, nums: List[int]) -> int:

        nums.sort()
        summ =0 
        count =0
        for i in range(len(nums)-1,-1,-1):
            summ += nums[i]
            if summ <= 0:
                return count
            count+=1
        return len(nums)
