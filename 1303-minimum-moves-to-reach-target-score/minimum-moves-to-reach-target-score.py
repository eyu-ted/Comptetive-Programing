class Solution:
    def minMoves(self, target: int, max_doubles: int) -> int:
        moves = 0
        if max_doubles == 0:
            return target - 1 
        while target > 1:

            if target %2  :
                target -= 1
                moves += 1
            else:
                target //= 2
                moves += 1
                max_doubles -= 1
                if max_doubles == 0:
                    return moves + (target-1) 
                
        
        return moves

        