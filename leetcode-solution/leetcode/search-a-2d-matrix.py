class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])
        row = len(matrix)

        l=-1
        r= col*row
        while r > l+1:
            mid = (r+l)//2
            mat_row = mid // col
            mat_col = mid % col

            if matrix[mat_row][mat_col] == target:
                return True
            elif  matrix[mat_row][mat_col] > target:
                r = mid 
            elif matrix[mat_row][mat_col] < target:
                l = mid
        return False
        