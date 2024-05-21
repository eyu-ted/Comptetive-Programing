class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo ={}

        def dfs(i,j):

            if (i,j) in memo:
                return memo[(i,j)]
            
            minn = float("inf")
            for k in range(i+1,j):
                minn = min(minn,(values[i]*values[j]*values[k] + dfs(k,j) + dfs(i,k)))
            
            memo[(i,j)] = minn if minn != float("inf") else 0
            return memo[(i,j)]
        return dfs(0,len(values)-1)

        