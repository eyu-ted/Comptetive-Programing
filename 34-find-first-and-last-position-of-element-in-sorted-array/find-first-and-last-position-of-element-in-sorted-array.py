class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first_pos():
            left = 0 
            right = len(nums)-1
            first = -1
            while right >= left:

                mid = (right+left) // 2

                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return first
        
        def last_pos():
            left = 0 
            right = len(nums)-1
            last = -1
            while right >= left:
                mid = (right+left) // 2

                if nums[mid] == target:
                    last = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return last
        
        return [first_pos(),last_pos()]

        