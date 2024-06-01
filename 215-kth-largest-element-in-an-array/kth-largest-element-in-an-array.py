class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ans = nlargest(k, nums)
        return ans[-1]