class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0]*n
        available  = [i for i in range(n)]
        used = []

        for start , end in meetings:

            while used and used[0][0] <= start:
                endd, room = heapq.heappop(used)
                heapq.heappush(available,room)
            
            if not available:
                end_time ,room = heapq.heappop(used)
                end = end_time + (end-start)
                heapq.heappush(available,room)
                
            
            r =heapq.heappop(available)
            heapq.heappush(used,(end,r))

            count[r]+=1
        return count.index(max(count))
        