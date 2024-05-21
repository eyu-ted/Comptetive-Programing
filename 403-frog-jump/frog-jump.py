class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = {}
        goal = stones[-1]
        sett= set(stones)
        def dfs(last,pos):
            if pos==goal:
                return True
            if pos>goal or pos<=0 :
                return False
            if pos not in sett:
                return False


            if (last,pos) in memo:
                return memo[(last,pos)]

            x = dfs(last,pos+last) or dfs(last+1,pos+last+1)
            if last>1:
                x = x or  dfs(last-1,pos+(last-1)) 
            memo[(last,pos)] =x


            return memo[(last,pos)]
        
        return dfs(1,1)
        