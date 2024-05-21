class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:


        def inbound(x,y):
            return x>-1 and x<len(matrix) and y>-1 and y<len(matrix[0])

        maxx= 0
        
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                matrix[i][j]=int(matrix[i][j])
                dia=right=bot=0
                if inbound(i+1,j+1):
                    dia += int(matrix[i+1][j+1])
                    
                if inbound(i,j+1):
                    right += int(matrix[i][j+1])
                if inbound(i+1,j):
                    bot += int(matrix[i+1][j])
                
                if int(matrix[i][j]):
                    matrix[i][j] += min(bot,min(right,dia)) 
                    maxx= max(maxx,matrix[i][j])
        
    
        return maxx*maxx
                


