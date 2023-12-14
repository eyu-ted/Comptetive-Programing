class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        set_num=set(nums)
        maxx=float("-inf")

        for n in nums:
            if n-1 not in set_num:
                i=0
                while n+i in set_num:
                    i+=1
                maxx=max(maxx,i)
        return maxx
