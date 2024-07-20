class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = {}
        def inbound(x,y):
            return x>=0 and x<len(matrix) and y>=0 and y<len(matrix[0])
        
        direction = [(1,0),(0,1),(0,-1),(-1, 0)]

        def dfs(r, c):
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 1
            for dr, dc in direction:
                if inbound(r+dr,c+dc) and matrix[r][c] < matrix[r+dr][c+dc]:
                    res = max(res, 1+dfs(r+dr,c+dc))
                
            dp[(r,c)] = res
            return res
        
        max_path = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_path = max(max_path,dfs(i, j))
        
        return max_path
        