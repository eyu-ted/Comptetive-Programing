class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
      
        from heapq import heappop, heappush
    
        intervals.sort(key=lambda x:x[0])  # O(nlog(n))
        n=len(intervals)
        h=[intervals[0][-1]]
        cpt=1

        #O(nlog(n))
        for i in range(1,n):#O(n)
            s,e=intervals[i]
            if s < h[0]:
                cpt+=1
                heappush(h,e)#O(log(n))
            else:
                heappop(h)#O(log(n))
                heappush(h,e)#O(log(n))
        #O(n) for space complexity
                
        return cpt