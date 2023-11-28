class Solution:
    def maxArea(self, height: List[int]) -> int:
        minn=float("inf")
        area=0
        r=len(height)-1
        l=0
        while r>l:
            minn=min(height[l],height[r])
            area=max(area,minn*(r-l))
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return area
            
        