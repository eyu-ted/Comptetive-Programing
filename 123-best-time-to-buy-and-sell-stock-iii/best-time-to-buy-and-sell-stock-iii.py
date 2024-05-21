class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}
        
        # @cache
        def dfs(i,buying,c):

            if i >= len(prices) or c==2:
                return 0
            

            if (i,buying,c) in memo:
                return memo[(i,buying,c)]
            

            if buying:
                memo[(i,buying,c)] = max(dfs(i+1,not buying,c)-prices[i],dfs(i+1,buying,c))
            else:
                memo[(i,buying,c)] = max(dfs(i+1,not buying,c+1)+prices[i],dfs(i+1,buying,c))
            
            return memo[(i,buying,c)]

        return dfs(0,True,0)


        