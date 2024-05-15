class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def inbound(x,y):
            return x<m and y<n
        dic ={}


        def dp(i,j):
            if not inbound(i,j):
                return 0

            if i==m-1 and j == n-1:
                return 1
            
            if (i,j) not in dic:
                dic[(i,j)] = dp(i+1,j) + dp(i,j+1)

            return dic[(i,j)]
        
        return dp(0,0)
    
    