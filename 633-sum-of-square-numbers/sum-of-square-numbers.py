from math import sqrt, floor

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(sqrt(c)) + 1):
            if floor(sqrt(c - i**2)) == sqrt(c - i**2):
                return True
        return False
