class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        time = {}
        adj = defaultdict(list)

        for u,v,t in times:
            adj[u].append((v,t))
        
        # print(adj)
        vis = set()
        heap = [(0,k)]
        while heap:

            takes,node = heapq.heappop(heap)

            if node in vis:
                continue
            vis.add(node)
            time[node] = takes

            for neigh, t in adj[node]:
                heapq.heappush(heap,(takes+t,neigh))
        

        # print(time)
        ans = max(time.values()) 
        return ans if ans != 0 and len(time) == n else -1



        