class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step = 0
        summ =0
       
        while summ<target or (summ-target)%2 != 0:
            step += 1
            summ += step
            
        return step
                
    