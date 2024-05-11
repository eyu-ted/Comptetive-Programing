class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxxheap=[]
        heapify(maxxheap)
        minnheap = [(capital[i],profits[i]) for i in range(len(profits)) ]
        heapify(minnheap)

        for i in range(k):
            while minnheap and minnheap[0][0]<=w:
                cap,prof = heappop(minnheap)
                heappush(maxxheap,-1*prof)
            if not maxxheap:
                break
            
            w+= -1*heappop(maxxheap)
        
        return w
        