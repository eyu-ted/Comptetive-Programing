class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while right >= left  :

            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            elif nums[right] >= nums[mid]:
                if nums[mid] <= target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid -1

            elif nums[left] <= nums[mid]:

                if nums[mid] >= target and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid  + 1
        
        return -1


        