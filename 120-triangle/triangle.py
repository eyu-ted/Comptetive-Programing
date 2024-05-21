class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo= {}

        def dfs(i,j):

            if i >= len(triangle) or len(triangle[i])<=j:
                return 0
            

            if (i,j) in memo:
                return memo[(i,j)]


            memo[(i,j)] = min(dfs(i+1,j)+triangle[i][j],dfs(i+1,j+1)+triangle[i][j])

            return memo[(i,j)]
        

        return dfs(0,0)