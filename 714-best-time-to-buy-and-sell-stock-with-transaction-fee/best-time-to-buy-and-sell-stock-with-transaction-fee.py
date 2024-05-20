class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo= {}

        def dfs(i,buying):
            if i >= len(prices):
                return 0
            
            if  (i,buying)  in memo:
                return memo[(i,buying)]
            if buying:
                buy = dfs(i+1,not buying) - prices[i]-fee
                notbuy = dfs(i+1,buying)
                memo[(i,buying)] = max(buy,notbuy)
            else:
                sell = dfs(i+1,not buying) + prices[i]
                notsell = dfs(i+1,buying)
                memo[(i,buying)] = max(sell,notsell)
            
            return memo[(i,buying)]
        
        return dfs(0,True)