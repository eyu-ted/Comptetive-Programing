class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x < 10:
            return True
        
        if x % 10 == 0:
            return False
        
        
        

        divisor = 1
        temp =x
        while temp >= 10:
            divisor *= 10
            temp //= 10

        while x:
            right_number = x%10
            left_number = x // divisor

            if right_number != left_number:
                return False

            # chopping the left number
            x %= divisor 
            #  chopping the right
            x //= 10
        

            divisor //= 100
        
        return True

            




        