class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row=[0]*len(grid)
        col=[0]*len(grid[0])
    

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                row[r]=max(grid[r][c],row[r])
                col[c]=max(grid[r][c],col[c])
   
        ans=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans+=min(row[r],col[c])-grid[r][c]
        return ans
        
                
        