class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count=0
        index=len(piles)-2
        ans=0
        while count<len(piles)//3:
            ans+=piles[index]
            index-=2
            count+=1
        return ans

        