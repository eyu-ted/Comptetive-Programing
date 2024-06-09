class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic={0:-1}
        total=0
        for i in range(len(nums)):
            total+=nums[i]
            rem=total%k
            if rem not in dic:
                dic[rem]=i
            elif i-dic[rem]>1:
                return True
        return False



        