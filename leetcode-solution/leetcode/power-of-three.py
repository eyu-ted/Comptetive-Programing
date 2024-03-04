class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<0:
            return False
        def helper(n):

            if n<1:
                return False
            elif n==1:
                return True

            x = helper(n/3) 

            return x

        return helper(n)