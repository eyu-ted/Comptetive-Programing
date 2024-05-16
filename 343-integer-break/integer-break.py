class Solution:
    def integerBreak(self, n: int) -> int:
        coins = [i for i in range(1,n)]
        dic={}
        print(coins)
        def dp(i,am):
            if am==0:
                return 1
            if am<0 :
                return 0

            if (i,am) not in dic:
                maxx = float("-inf")
                for c in coins:
                    maxx = max(maxx,dp(i+1,am-c)*c)
                dic[(i,am)]=maxx
                
            return dic[(i,am)]
        
     

 
        return dp(0,n)
                 


        