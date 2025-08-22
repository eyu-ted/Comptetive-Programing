class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(k):

            count  = 0
            for num in piles:
                count += math.ceil(num/k)
            
            return count <= h


        l = 1
        r = max(piles)

        while r >= l:

            mid = (l+r)//2

            if check(mid):
                r = mid - 1 
            else:
                l = mid +1
        return l



        