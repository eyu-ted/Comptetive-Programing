class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(i,lis):
            summ = sum(lis)
            if summ == target:
                result.append(lis.copy())
            
            if summ >target:
                return
            
            for j in range(i,len(candidates)):
                lis.append(candidates[j])
                backtrack(j,lis)
                lis.pop()
        
        backtrack(0,[])

        return result
