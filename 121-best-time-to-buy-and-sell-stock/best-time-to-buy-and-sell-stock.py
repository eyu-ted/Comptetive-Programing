class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        maxx = 0

        for r in range(len(prices)):
            if prices[r] > prices[l] :
                maxx = max(maxx, prices[r]-prices[l])
            else:
                l = r
        return maxx