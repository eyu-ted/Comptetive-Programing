class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # lastindex=len(nums)-1
        # for i in range(len(nums)-1,-1,-1):
        #     if i+nums[i]>=lastindex:
        #         lastindex=i
        # return True if lastindex==0 else False

        step=nums[0]
        i=0
        for i in range(len(nums)):
            if nums[i]+i>step:
                step=nums[i]+i
            if step==i:
                if i ==len(nums)-1:
                    return True
                else:
                    return False
        
        return True
                


