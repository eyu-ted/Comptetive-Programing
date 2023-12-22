class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            sett=set()
            for j in range(9):
                if board[i][j]!="." and board[i][j] in sett:
                    return False
                sett.add(board[i][j])
        
        for num in zip(*board):
            sett=set()
            for n in list(num):
                if n !="." and n in sett:
                    return False
                sett.add(n)

        for i in range(0,9,3):
            counti=0
            l=0
            for _ in range(3):
                sett=set()
                for _ in range(9):
                    if board[i][l]!="." and board[i][l] in sett:
                        return False
                    sett.add(board[i][l])
                    i+=1
                    counti+=1
                    if counti==3:
                        l+=1
                        counti=0
                        i-=3
                    
                        
        return True
        