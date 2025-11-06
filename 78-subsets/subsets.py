class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sett = set()

        def dfs(i, path):
            if i>len(nums):
                return
            if tuple(sorted(path)) not in sett:
                sett.add(tuple(sorted(path.copy())))
            
            for j in range(i,len(nums)):
                path.append(nums[j])
                dfs(j+1, path)
                path.pop()
        dfs(0,[])
        return list(sett)
        