class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        posZero=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    posZero.append([i, j])
        for i, j in posZero:     
            for row in range(len(matrix)):
                matrix[row][j]=0
            for col in range(len(matrix[0])):
                matrix[i][col]=0