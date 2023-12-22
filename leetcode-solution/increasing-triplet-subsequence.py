class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        small=float("inf")
        second_small=float("inf")
        for n in nums:
            if n <=small:
                small=n
            elif n<=second_small:
                second_small=n
            else:
                return True
        return False
        
        

            
        


        