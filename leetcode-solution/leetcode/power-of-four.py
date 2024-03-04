class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<0:
            return False
        def helper(n):
            if n<1:
                return False
            elif n==1:
                return True
            
            x = helper(n/4)

            return x
        return helper(n) 
        