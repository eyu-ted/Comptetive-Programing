class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        area = 0
        for i in range(len(height)):
            
            while stack and stack[-1][0] < height[i]:
                bottom,index = stack.pop()
                if stack:
                    block1 = stack[-1][0]
                    h = min(block1,height[i]) - bottom
                    w = i-stack[-1][1]-1
                    area += h*w
                    # print(area,h,w,i) 
            stack.append((height[i],i))

        
        return area