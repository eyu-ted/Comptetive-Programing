class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        memo = {}
        memo[2] = 1

        def dp(num):

            if num in memo:
                return memo[num]
            
            count = 0
            if num % 2 == 0:

                count = dp(num // 2) + 1 
            else:
                count = dp(3 * num + 1 ) + 1
            
            memo[num] = count

            return memo[num]
        
        result = []
        for nu in range(lo,hi+1):
            result.append((dp(nu),nu))
        
        result.sort()


        return result[k-1][1]

