class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [num*-1 for num in nums]
        heapq.heapify(nums)
        res = 0
        while k and nums:
            res = heapq.heappop(nums)
            k-=1
        return res*-1
        