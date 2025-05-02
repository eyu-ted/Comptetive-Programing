class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        '''
        Example with 
                \U0001d45b =   3
                no_odds = (3 + 1) // 2 = 4 // 2 = 2
                no_evens = 3 // 2 = 1
        '''

        # Calculate the count of good numbers for even and odd positions
        no_evens = (n + 1) // 2 #
        no_odds = n // 2 #02468

        # Calculate the count of good numbers based on the constraints
        odd_count = pow(4, no_odds, MOD)
        even_count = pow(5, no_evens, MOD)

        # Calculate the total count of good numbers
        total_count = (odd_count * even_count) % MOD
        
        return total_count
