class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dp ={}
        def inbound(x,y):
            return x<len(grid) and x>-1 and y<len(grid[0]) and y>-1
        direction =[(0,1),(1,0)]
        def dfs(i,j):
            if i == len(grid)-1 and j == len(grid[0])-1:
                return grid[i][j]
            if (i,j) in dp:
                return dp[(i,j)]

            minn = float("inf")

            for dr,dc in direction:
                if inbound(i+dr,j+dc):
                    minn =min(minn, dfs(i+dr,j+dc))
            
            dp[(i,j)] = grid[i][j] + minn
            
            return dp[(i,j)]


        return dfs(0,0)
            

            