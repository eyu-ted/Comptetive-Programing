class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currsum=sum(nums[:k])
        maxx=currsum/float(k)
        l=0
        for  r in range(k,len(nums)):
            currsum+=nums[r]
            currsum-=nums[l]
            l+=1
            maxx=max(maxx,currsum/float(k))
        return maxx

        