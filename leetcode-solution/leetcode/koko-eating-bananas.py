class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.total = sum(piles)
        maxx =  max(piles)
        minn = 1
        
        def isPossible(per):
            tot = 0
            for n in piles:
                tot += ceil(n/per)
            return tot <= h
            
        while minn <= maxx:

            mid = (minn+maxx)//2
            if isPossible(mid):
                maxx = mid-1
            else:
                minn = mid + 1
        return minn