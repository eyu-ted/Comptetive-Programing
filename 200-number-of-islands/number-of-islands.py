class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(1,0), (0,1), (-1,0),(0,-1)]

        def inbound(x,y):
            return x>-1 and x<len(grid) and y>-1 and y<len(grid[0])
        
        count = 0

        def bfs(i,j):

            queue = deque()
            queue.append((i,j))

            while queue:
                row , col = queue.pop()
                grid[row][col] = "0"
                

                for dr,dc in direction:
                    new_row , new_col = row+dr , col+dc
                    if inbound(new_row,new_col)  and grid[new_row][new_col] == "1":
                        queue.append((new_row,new_col))
                        # visited.add((new_row,new_col))

                        


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    bfs(row,col)
                    count+=1
        return count
