class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minn = float("inf")
        res = float("-inf")
        for price in prices:
            minn = min(minn, price)
            if price - minn > res:
                res = price - minn
        
        return res
            
            


