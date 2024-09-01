class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def inbound(x,y):
            return x < len(matrix) and x>-1 and y<len(matrix[0]) and y>-1
        direction = [(1,0),(0,1),(1,1)]
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                matrix[i][j] = int(matrix[i][j])
                minn = float("inf")
                for dr, dc in direction:
                    if inbound(i+dr,j+dc):
                        minn = min(minn ,matrix[i+dr][j+dc])
                    
                    else:
                        minn = 0
                        break
                if matrix[i][j]:
                    matrix[i][j] += minn
        

        ans = float("-inf")
        print(matrix)
        for nums in matrix:
            nums.append(ans)
            ans = max(nums)
        return ans**2



        