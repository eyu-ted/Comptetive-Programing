class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l=0
        count=0
        minn=float("inf")
        for r in range(len(blocks)):
            if blocks[r]=="W":
                count+=1
            if r>=k - 1:
                minn=min(minn,count)
                if blocks[l]=="W":
                    count-=1
                l+=1
               
        return minn if minn!=float("inf") else count
            

