class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row =set()
        col = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        # print(sett)
        for i in range(len(matrix)):

            for j in range(len(matrix[0])):
                if i in row:
                    matrix[i][j] =0


                if j in col:
                    matrix[i][j] =0
    
        