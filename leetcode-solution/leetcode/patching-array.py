class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i=0
        c=1
        ans=0
        while c <=n:
            if i<len(nums) and nums[i]<=c:
                c+=nums[i]
                i+=1
                
            else:
                ans+=1
                c=c*2 
                
                

            
        return ans
        




        
        