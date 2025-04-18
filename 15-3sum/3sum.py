class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        nums.sort()
        answer = set()
        for index in range(len_nums):
            left, right = index+1, len_nums-1
            while left < right:
                if nums[left]+nums[right]+nums[index] == 0:
                    answer.add((nums[index], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left]+nums[right] +nums[index] > 0:
                    right -= 1
                else:
                    left += 1
        
        return list(answer)
