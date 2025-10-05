class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            result = []
            def backtrack(lis):

                if len(lis) == len(nums):
                    result.append(lis.copy())
                

                for j in range( len(nums)):
                    if nums[j] not in lis:
                        lis.append(nums[j])
                        backtrack(lis)
                        lis.pop()
            backtrack([])

            return result
