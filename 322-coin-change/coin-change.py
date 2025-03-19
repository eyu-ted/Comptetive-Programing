class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(am):
            if am in cache:
                return cache[am]
            if am == 0:
                return 0
            if am < 0:
                return float('inf') 

            min_count = float('inf')
            for coin in coins:
                res = dfs(am - coin)
                if res != float('inf'):  
                    min_count = min(min_count, res + 1)

            cache[am] = min_count
            return cache[am]

        result = dfs(amount)
        return result if result != float('inf') else -1
