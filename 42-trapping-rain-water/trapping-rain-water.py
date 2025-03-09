class Solution:
    def trap(self, height: List[int]) -> int:

        total = 0
        stack = []

        for i in range(len(height)):

            while stack and stack[-1][0] < height[i]:
                pop, _ = stack.pop()
                if stack:
                    width = i - stack[-1][1] - 1 
                    hght = min(height[i],stack[-1][0]) - pop
                    total += (hght*width)

                

            stack.append((height[i],i)) 


        return total
        