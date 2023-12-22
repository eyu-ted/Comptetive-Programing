class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i=0
        for nums in zip(*matrix):
            matrix[i]=list(nums)[::-1]
            i+=1
        return matrix
        