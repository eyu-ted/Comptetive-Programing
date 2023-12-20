class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l=len(matrix)
        ans=[[0]*l for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j][i]=matrix[i][j]
        return ans
        