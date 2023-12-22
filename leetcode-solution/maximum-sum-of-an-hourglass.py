class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxx=float("-inf")
        total=0
        for i in range(len(grid)):
            for j in range(1,len(grid[0])-1):
                if i+2 < len(grid):
                    total=grid[i][j]+grid[i][j+1]+grid[i][j-1]+grid[i+1][j]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j-1]
                maxx=max(maxx,total)
        return maxx

        
        


    

        