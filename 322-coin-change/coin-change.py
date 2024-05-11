class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        
        def dp(am):
            
            if am ==0:
                return 0
            if am<0:
                return float("inf")
            
            if am not in memo:
                minn =float("inf")
                for n in coins:
                    minn =min(minn,dp(am-n)+1)
                memo[am] =minn
            return memo[am]
        

        
        x=dp(amount) 
   
        return x if  x!=float("inf") else  -1
            
        
        

        