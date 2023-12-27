class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        seen={}
        x=0
        y=len(mat[0])-1
        summ=0
        for _ in range(len(mat)):
            if x<len(mat) and y>=0:
                summ+=mat[x][y]
                seen[(x,y)]=1
                x+=1
                y-=1
        x=0
        y=0
        for _ in range(len(mat)):
            if x<len(mat) and y<len(mat[0]) and (x,y) not in seen:
                summ+=mat[x][y]
            x+=1
            y+=1
        return summ


