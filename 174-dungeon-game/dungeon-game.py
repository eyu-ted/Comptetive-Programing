class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        def inbound(x,y):
            return x < len(dungeon) and x>-1 and y < len(dungeon[0]) and y >- 1
        

        for i in range(len(dungeon)-1,-1,-1):
            for j in range(len(dungeon[0])-1,-1,-1):

                maxx = float("-inf")

                if inbound(i,j+1):
                    maxx = max(maxx , dungeon[i][j+1])
                
                if inbound(i+1,j):
                    maxx = max(maxx , dungeon[i+1][j])
                

                if maxx == float("-inf"):
                    maxx =0
                
                dungeon[i][j] += maxx

                if dungeon[i][j] > 0:
                    dungeon[i][j] =0
        print(dungeon)
        return (dungeon[0][0]*-1)+1


        