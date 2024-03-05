class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.prev=0
    

        def back(start,path):

            
            if path not in ans:
                if sum(path) == target:
                    ans.append(path[:])
                    return 

            for i in range(start,len(candidates)):
                path.append(candidates[i])
                if self.prev != candidates[i] and sum(path) <= target:
                    back(i+1,path)
                self.prev = path.pop()
        back(0,[])

        return ans
        