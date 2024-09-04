class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxx = float("-inf")

        


        check = [[0]*(len(grid[0])) for i in range(len(grid))]

        visited = set()

        direction = [(1,0),(0,1),(-1,0),(0,-1)]

        def inbound(x,y):
            return x<len(grid) and x>-1 and y<len(grid[0]) and y>-1

        def bfs(i,j):
            nonlocal count 
            visited.add((i,j))
            for dr ,dc in direction:
                if inbound(i+dr,j+dc):
                    if (i+dr,j+dc) not in visited and grid[i+dr][j+dc] ==1:
                        count+=1
                        bfs(i+dr,j+dc)


        for i in range(len(grid)):
            for j in range(len(grid[0])):

                count = 0
                if grid[i][j] == 1 and (i,j) not in visited:
                    count =1
                    bfs(i,j)
                maxx = max(maxx,count)
        return maxx


