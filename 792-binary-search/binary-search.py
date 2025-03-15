class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = -1
        high = len(nums) 
        
        while low + 1 < high :
            mid = low + (high-low)//2
            
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                low = mid
            else:
                high = mid

        return -1