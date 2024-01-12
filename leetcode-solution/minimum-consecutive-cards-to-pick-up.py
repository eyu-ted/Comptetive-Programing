class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l=0
        r=1
        minn=float("inf")
        dic=defaultdict(int)
        for r in range(len(cards)):
            dic[cards[r]]+=1
            while dic[cards[r]]>1:
                dic[cards[l]]-=1
                if dic[cards[l]]==0:
                    dic.pop(cards[l])
                minn=min(minn,r-l+1)
                l+=1         
        return minn if minn != float("inf") else -1

