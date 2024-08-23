class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        matrix= []

        for _ in range(len(grid)):
            matrix.append([float("inf")]*len(grid[0]))


        def inbound(x,y):
            return x>-1 and x<len(grid) and y>-1 and y<len(grid[0])


        direction = [(1,0),(0,1)]

        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                
                minn = float("inf")
                for dr ,dc in direction:
                    if inbound(i+dr,j+dc) :
                        minn = min(minn,grid[i+dr][j+dc])
                if minn ==float("inf"):
                    minn =0
                grid[i][j] += minn

        

        return grid[0][0]




            