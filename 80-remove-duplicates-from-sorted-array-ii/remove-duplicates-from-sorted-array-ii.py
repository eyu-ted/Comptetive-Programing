class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        dic={}
        x=0
        for i in range(len(nums)):
            dic[nums[i]]=1+dic.get(nums[i],0)
            if dic[nums[i]]<=2:
                nums[x]=nums[i]
                x+=1
        return x

        