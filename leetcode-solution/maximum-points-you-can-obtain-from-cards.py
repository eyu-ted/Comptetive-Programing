class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lis=cardPoints[len(cardPoints)-k:]+cardPoints[:k]
        total=0
        l=0
        maxx=float("-inf")
        for r in range(len(lis)):
            total+=lis[r]
            if r>=k:
                total-=lis[l]
                l+=1
            maxx=max(maxx,total)
        return maxx


        


        