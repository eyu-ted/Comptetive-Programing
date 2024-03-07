class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path =set()

        def backtrack(row , col , indx):
            if indx==len(word):
                return True

            if row<0 or col <0 or row >=len(board) or col >= len(board[0]) or  word[indx] != board[row][col] or (row,col) in path :
                return False

            path.add((row,col))

            res = backtrack(row+1,col,indx+1) or backtrack(row,col+1,indx+1) or backtrack(row-1,col,indx+1) or backtrack(row, col-1,indx+1)

            path.remove((row,col))

            return res



        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        return False    
        