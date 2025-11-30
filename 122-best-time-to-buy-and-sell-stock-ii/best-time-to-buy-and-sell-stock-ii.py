class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        minn = prices[0]
        for i in range(1,len(prices)):

            if prices[i]< prices[i-1]:
                res += prices[i-1] - minn
                minn = prices[i]
            
            # minn = min(minn,prices[i])
        res += prices[-1] - minn
        
        return res