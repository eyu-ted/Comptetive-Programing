class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cheap = [float("inf")]*n

        cheap[src] = 0

        temp = cheap[:]
        for i in range(k+1):
            
            for u,v,c in flights:
                if cheap[u] != float("inf") and cheap[u]+c < temp[v]:
                    temp[v] = cheap[u]+c
            
            cheap = temp[:]
                    
                    
                    
            
        
       

        return cheap[dst] if cheap[dst] != float("inf") else -1