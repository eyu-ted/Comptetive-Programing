class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def inbound(x, y):
            return x > -1 and y > -1 and x < len(matrix) and y < len(matrix[0])
        
        rows, cols = len(matrix), len(matrix[0])
        ans = [[float("inf")] * cols for _ in range(rows)]
        
        
        for j in range(cols):
            ans[0][j] = matrix[0][j]
        

        for i in range(1, rows):
            for j in range(cols):
                if inbound(i - 1, j - 1):
                    ans[i][j] = min(ans[i][j], matrix[i][j] + ans[i - 1][j - 1])
                if inbound(i - 1, j):
                    ans[i][j] = min(ans[i][j], matrix[i][j] + ans[i - 1][j])
                if inbound(i - 1, j + 1):
                    ans[i][j] = min(ans[i][j], matrix[i][j] + ans[i - 1][j + 1])
        
        
        return min(ans[-1])
