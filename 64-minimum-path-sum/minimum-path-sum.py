class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def inbound(x,y):
            return x < len(grid) and x>-1 and y < len(grid[0]) and y>-1
        direction = [(1,0),(0,1)]
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                minn = float("inf")
                for dr ,dc in direction:
                    if inbound(i+dr,j+dc):
                        minn = min(minn,grid[i+dr][j+dc])
                if minn == float("inf"):
                    minn = 0
                grid[i][j] += minn
        return grid[0][0]



        