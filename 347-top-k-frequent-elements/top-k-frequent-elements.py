class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = defaultdict(int)

        for num in nums:
            dic[num] += 1
        
        heap = []
        for num, ferquency in dic.items():
            heapq.heappush(heap,(-1 * ferquency, num))
        
        result = []

        while k:
            frequency, num = heapq.heappop(heap)
            result.append(num)
            k -= 1
        
        return result
        