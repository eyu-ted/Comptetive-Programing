class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1] * n
        right = [n] * n

        stack = []
        for i in range(n):

            while stack and heights[stack[-1]] > heights[i]:
                right[stack[-1]] = i
                stack.pop()
            
            if stack:
                left[i] = stack[-1]
            
            stack.append(i)
        
        
        max_area = float("-inf")
        for index , height in enumerate(heights):
            width = (right[index] - left[index] - 1)
            max_area = max(max_area, height * width )
            
        return max_area

