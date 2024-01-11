class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        dic={}
        l=0
        maxx=float("-inf")
        for r in range(len(nums)):
            dic[nums[r]]=1+dic.get(nums[r],0)
            while 0 in dic and dic[0]==2:
                if nums[l]==0:
                    dic[0]-=1
                l+=1
            maxx=max(maxx,r-l)
            
        return maxx



        