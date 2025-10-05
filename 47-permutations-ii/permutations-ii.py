class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = set()
        def backtrack(lis):

            if len(lis) == len(nums) and tuple(lis) not in res:
                temp = []
                for indx, num in lis:
                    temp.append(num)
                res.add(tuple(temp))
                return


            for j in range(len(nums)):
                if (j,nums[j]) not in lis:
                    lis.append((j,nums[j]))
                    backtrack(lis)
                    lis.pop()
        
        backtrack([])
        
        return list(res)
                
        