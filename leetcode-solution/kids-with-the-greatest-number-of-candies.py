class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx=max(candies)
        l=len(candies)
        ans=[True]* l
        for i in range(l):
            if candies[i]+extraCandies<maxx:
                ans[i]=False
        return ans
        