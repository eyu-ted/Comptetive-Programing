class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # weights.sort()
        def check(cap):

            day = 1
            count = 0
            for num in weights:
                
                if count + num > cap:
                    count = 0
                    day +=1
                
                count += num
        
            return day <= days
                    
        l = max(weights)
        r = sum(weights)

        while r >=l:

            mid = (l+r) //2 

            if check(mid):
                r = mid  -1
            else:
                l = mid + 1

        return l
        
        
