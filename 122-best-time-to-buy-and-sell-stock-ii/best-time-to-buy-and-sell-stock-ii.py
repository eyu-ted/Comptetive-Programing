class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prev = prices[0]
        ans = 0
        for i in range(1,len(prices)):

            if prices[i] > prev:
                if i+1 < len(prices) and prices[i+1] <= prices[i]:
                    ans += (prices[i]-prev)
                    prev = float("inf")
            
            else:
                prev = prices[i]
        
        if  prices[-1]> prev:
            ans += prices[i]-prev
        return ans



        