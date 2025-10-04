class Solution:
    def reorganizeString(self, s: str) -> str:

        count = Counter(s)

        max_freq = max(count.values())

        if max_freq > ceil(len(s)/2):
            return ""
        
        heap = []

        for key in count:
            heap.append([-1 * count[key],key])
        heapq.heapify(heap)
        
        
        result = ""

        while heap:
            count , ch = heapq.heappop(heap)
            if result:
                if result[-1] != ch:
                    count +=1
                    result +=ch
                    if count <0:
                        heapq.heappush(heap,[count, ch])
                else:
                    count2,ch2 = heapq.heappop(heap)
                    count2 +=1
                    result +=ch2
                    if count2 <0:
                        heapq.heappush(heap,[count2,ch2])
                    heapq.heappush(heap,[count, ch])
            else:
                count +=1
                result +=ch
                if count <0:
                    heapq.heappush(heap,[count, ch])

                    

        return result
        