class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxx=float("-inf")
        for n in nums:
            if n==1:
                count+=1
            else:
                maxx=max(count,maxx)
                count=0
        return max(count,maxx) if maxx!=float("-inf") else len(nums)
        