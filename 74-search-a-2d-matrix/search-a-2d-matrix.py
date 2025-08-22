class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # 0 - 11 ->  3%4 =->3 -> j
        #             4%4 ->0  j
        #             11%4 -> 3 j

        #             3//4 ->0 ->i
        #             4//4 -> ->i
        #             8//4 >2 ->i

        l=0
        r = (len(matrix)*len(matrix[0])) - 1

        while r >= l:

            mid = (l+r) //2 

            i = mid // (len(matrix[0]))
            j = mid % len(matrix[0])

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] >target:
                r = mid -1
            else:
                l = mid +1 
        return False

        