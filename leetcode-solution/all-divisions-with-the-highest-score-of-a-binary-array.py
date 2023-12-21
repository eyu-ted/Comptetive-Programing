class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        maxx=rightsum=nums.count(1)
        leftsum=0
        ans=[]
        for i in range(len(nums)+1):
            total=leftsum+rightsum
            if maxx<total:
                ans=[i]
                maxx=total
            elif maxx==total:
                ans.append(i)
            if i<len(nums):
                if nums[i]==0:
                    leftsum+=1
                else:
                    rightsum-=1
        return ans
            
                
        
        