class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = Counter(nums)
        lis = []
        for key,val in dic.items():
            lis.append((-1*val , key))
        
        heapq.heapify(lis)
        ans = []
        for _ in range(k):
            ans.append(heappop(lis)[1])
        
        return ans
        