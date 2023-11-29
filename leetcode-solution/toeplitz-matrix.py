class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        for r in range(row):
            for i in range(col):
                if i+1<col and r+1 < row and matrix[r][i]!=matrix[r+1][i+1]:
                    return False
        return True