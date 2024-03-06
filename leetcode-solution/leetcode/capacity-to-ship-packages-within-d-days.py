class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        minn = max(weights)
        maxx = sum(weights)

        def isPossible(n):
            tot = 0
            d =1
            for i in range(len(weights)):
                
                if tot + weights[i] > n:
                    d += 1
                    tot = 0
                tot += weights[i]
            return d <= days
        
        while maxx >= minn:

            mid =(maxx+minn)//2
            if isPossible(mid):
                maxx = mid-1
            else:
                minn = mid+1
        return minn
        
    



        