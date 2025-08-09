class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        l = 0 
        r = 1
        while r<len(prices):
            
            if prices[r] > prices[l]:
                if r+1<len(prices) and prices[r+1] >= prices[r]:
                    r += 1
                    continue
                else:
                    profit += prices[r] - prices[l]
                    l = r
            else:
                l = r

            r += 1
        
                    
        return profit + prices[r-1] - prices[l]
                
            
            
            

            
            




        