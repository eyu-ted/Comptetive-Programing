class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(i,lis):

            res.append(lis.copy())

            for j in range(i,len(nums)):
                lis.append(nums[j])
                backtrack(j+1,lis)
                lis.pop()
        
        backtrack(0,[])

        return res