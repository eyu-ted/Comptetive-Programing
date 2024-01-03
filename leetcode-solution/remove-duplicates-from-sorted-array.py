class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # dic={}
        # x=0
        # for i in range(len(nums)):
        #     if nums[i] not in dic:
        #         dic[nums[i]]=1
        #         nums[x]=nums[i]
        #         x+=1
        # return x
        if len(nums)==1:
            return 1
        l=0
        r=1
        count=1
        i=0
        while r<len(nums):
            if nums[l]!=nums[r]:
                nums[i]=nums[l]
                i+=1
                nums[i]=nums[r]
                count+=1
            l+=1
            r+=1

        return count 

    
