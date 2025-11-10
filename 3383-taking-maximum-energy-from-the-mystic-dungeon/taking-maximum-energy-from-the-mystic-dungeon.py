class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:


        memo = {}

        def dp(i):

            if i >= len(energy):
                return 0
            
            if i in memo:
                return memo[i]
            
            total = dp(i+k) + energy[i]
            memo[i] = total
            return memo[i]
        maxx = float("-inf")

        for i in range(len(energy)):
            maxx = max(maxx,dp(i))
        return maxx
            

        