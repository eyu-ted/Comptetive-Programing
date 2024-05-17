class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n =len(obstacleGrid[0])
        m =len(obstacleGrid)

        dp=[[0]*n for _ in range(m)]

        if obstacleGrid[m-1][n-1] == 1:
            return 0


        dp[m-1][n-1] = 1


        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):

                if i+1<m:
                    if obstacleGrid[i][j] != 1:

                        dp[i][j]+=dp[i+1][j]
                if j+1<n:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j]+=dp[i][j+1]
        

        return dp[0][0]
        