class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        maxx =max(houses[-1],heaters[-1])
        minn = 0

        def isPossible(n):
            
            h = 0
            ho = 0

            while len(houses)>ho and len(heaters)>h:
                if abs(houses[ho]-heaters[h]) <= n:
                    ho+=1
                else:
                    h+=1
            
               
            return len(houses) == ho and len(heaters) != h
        
        
   

        while minn <= maxx:
            mid = (minn+maxx)//2

            if isPossible(mid):
                maxx = mid - 1
            else:
                minn = mid + 1
        return minn



        