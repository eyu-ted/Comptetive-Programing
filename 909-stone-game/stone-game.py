class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
    
        dic={}
        def dp(l,r,flag):
            if l>r:
                return 0
            
            if (l,r) not in dic:

                if flag :
                    left= piles[l]
                    right=0
                else:
                    right = piles[r]
                    left=0
                dic[(l,r)] = max(dp(l+1,r,not flag)+left,dp(l,r-1,not flag)+right)
            return dic[(l,r)]
        return dp(0,len(piles)-1,True) > sum(piles)/2



            
    
