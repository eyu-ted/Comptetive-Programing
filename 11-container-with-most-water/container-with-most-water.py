class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        ans = float("-inf")

        while right>left:
            h = min(height[left],height[right])
            width = right-left
            area = h*width
            ans = max(ans,area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return ans








        