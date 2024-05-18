class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        candidates.sort()

        def back(start , path):

            if path not in ans:
                if sum(path) == target:
                    ans.append(path[:])
                    return 
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                if sum(path)<=target:
                    back(i , path)
                path.pop()
            
        back(0,[])

        return ans

            
        