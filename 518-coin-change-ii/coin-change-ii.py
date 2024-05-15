class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dic={}

        def dp(i,am):

            if am == 0:
                return 1
            if am<0 or i==len(coins):
                return 0
            
            if (i,am) not in dic:
                take = dp(i,am-coins[i])
                nottake = dp(i+1,am)
                dic[(i,am)] = take + nottake
            
            return dic[(i,am)]


        return dp(0,amount)


        