class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        nums.sort()
        def backtrack(i,lis):
            
            if tuple(lis) not in result:
                
                result.add(tuple(lis.copy()))
            


            for j in range(i,len(nums)):

                lis.append(nums[j])

                backtrack(j+1, lis)
                lis.pop()
        

        backtrack(0,[])
        return list(result)