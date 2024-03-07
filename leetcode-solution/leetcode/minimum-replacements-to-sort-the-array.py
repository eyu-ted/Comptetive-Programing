class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[len(nums)-1]
        count=0

        for i in range(len(nums)-2,-1,-1):
            step = nums[i]//last
            if nums[i] % last != 0:
                step+=1
                last = nums[i]//step
            count += step -1
        return count
        