class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap =[1]

        heapq.heapify(heap)
        sett =set()
        c=0

        while True:
            p = heapq.heappop(heap)
            c+=1
            if c==n:
                return p

            if p*2 not in sett:

                heapq.heappush(heap,p*2)
                sett.add(p*2)
        
            
            if p*3 not in sett:
                heapq.heappush(heap,p*3)
                sett.add(p*3)
            
            if p*5 not in sett:
                heapq.heappush(heap,p*5)
                sett.add(p*5)
            

