class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        memo={}
        col = len(dungeon[0])-1
        row = len(dungeon)-1
        def inbound(x,y):
            return x>-1 and x<len(dungeon) and y>-1 and y<len(dungeon[0])

        def dfs(i,j):

            if not inbound(i,j):
                return float("-inf")
            if i==row and j==col:
                return dungeon[row][col] if dungeon[row][col] <0 else 0
            
            if (i,j) in memo:
                return memo[(i,j)]

            memo[(i,j)] = max(dfs(i,j+1)+dungeon[i][j],dfs(i+1,j)+dungeon[i][j])

            if memo[(i,j)] >0:
                memo[(i,j)]=0
            


            return memo[(i,j)]

        return abs(dfs(0,0))+1
        