class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for p in range(33):
            if 2**p==n:
                return True
        return False
        