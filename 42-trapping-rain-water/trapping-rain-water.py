class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        area = 0

        for i in range(len(height)):

            while stack and stack[-1][0] < height[i]:
                bottom,indx = stack.pop()
                if stack:
                    wall = stack[-1][0]
                    h = min(height[i],wall) -bottom
                    w = i - stack[-1][1]-1
                    area += h*w
                    

            stack.append([height[i],i])
        

        return area