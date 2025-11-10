class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        from heapq import heappop, heappush

        h = []

        heappush(h,[grid[0][0],0,0])

        visited = set()
        visited.add((0,0))
        maxx = float("-inf")

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(x,y):
            return x>-1 and y>-1 and x<len(grid) and y<len(grid[0])
        while h:
            val,row,col = heappop(h)
            maxx = max(maxx,val)
            if (row,col) == (len(grid)-1, len(grid[0])-1):
                break
            for dr,dc in directions:
                new_row, new_col = row+dr, col + dc

                if inbound(new_row,new_col) and (new_row,new_col) not in visited:
                    heappush(h,[grid[new_row][new_col], new_row,new_col])
                    visited.add((new_row,new_col))
        
        return maxx

