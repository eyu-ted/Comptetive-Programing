class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = float("-inf")
        while left < right:

            max_area = max(max_area , (min(height[left], height[right]) * (right - left)) )

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        
        return max_area