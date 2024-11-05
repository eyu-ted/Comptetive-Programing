class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # ans = nlargest(k, nums)
        # return ans[-1]

        lis = []

        for num in nums:
            lis.append(num*-1)

        heapq.heapify(lis) 
        ans = 0

        for _ in range(k):
            ans = heappop(lis)
        
        return ans*-1


