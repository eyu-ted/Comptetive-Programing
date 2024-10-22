class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = m-1
        r = n-1

        return math.comb(r+d,d)
        