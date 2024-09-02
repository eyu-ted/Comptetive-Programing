class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        

        def dfs(i,first):
            if first:
                if i >= len(nums)-1 :
                    return 0
            else:
                if i >= len(nums) :
                    return 0 

            if i in dp:
                return dp[i]
            
        
                    


            dp[i] = max(dfs(i+1,first),dfs(i+2,first)+nums[i])

            return dp[i]
        dp ={}
        maxx = float("-inf")
        maxx = max(maxx, dfs(0,True) )
        dp = {}
        maxx =  max(maxx ,dfs(1,False))
        return maxx 