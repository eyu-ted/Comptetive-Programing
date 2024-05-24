class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dic= {}
        def dfs(summ):

            if summ == target:
                return 1
            if summ > target:
                return 0
            
            if summ in dic:
                return dic[summ]
            dic[summ] = 0
            for num in nums:
                dic[summ] += dfs(summ+num)
            
            return dic[summ]
        return dfs(0)
        # dp = [0]*(target+1)
        # dp[0]=1
        # for i in range(1,target+1):
        #     for j in nums:
        #         if i>=j:
        #             dp[i]  += dp[i-j]
        # print(dp)
        # return dp[-1]
        