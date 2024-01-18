class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefsum=[0]*(len(nums)+1)
        for request in requests:
            prefsum[request[0]]+=1
            prefsum[request[1]+1]-=1
        for i in range(1,len(prefsum)):
            prefsum[i]+=prefsum[i-1]
        nums.sort()
        nums=[0]+nums
        prefsum.sort()
        ans=0
        print(nums)
        print(prefsum)
        for i in range(len(nums)):
            ans+=prefsum[i]*nums[i]
        return ans%(10**9+7)
