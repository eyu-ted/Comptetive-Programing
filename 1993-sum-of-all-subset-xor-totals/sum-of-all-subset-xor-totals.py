class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def backtrack(i,lis):

            nonlocal res
            
            res += lis
            
            for j in range(i,len(nums)):
                lis ^= nums[j]
                backtrack(j+1,lis)
                lis ^= nums[j]

        
        backtrack(0,0)

        return res



        