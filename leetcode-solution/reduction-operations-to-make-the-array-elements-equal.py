class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # # hashset=list(set(nums))
        # ans=0
        # seen=set()
        # # for i in range(len(nums)):
        # #     for j in range(len(hashset)):
        # #         if nums[i]>hashset[j]:
        # #             ans+=1
        # dic={}
        # for n in nums:
        #     if n in seen:
        #         n


        # return ans
        nums.sort()
        count=0
        prev=0
        ans=0
        for n in nums[::-1]:
            
            if prev!=n:
                ans+=count

            prev=n
            count+=1
            
    
        return ans
        
        