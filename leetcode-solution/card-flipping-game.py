class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        minn=float("inf")
        f=set()
        for i,n in enumerate(fronts):
            if n==backs[i]:
                f.add(n)

        for n in fronts+backs:
            if n not in f:
                minn=min(minn,n)
        return minn if minn!=float("inf") else 0



            
                
        