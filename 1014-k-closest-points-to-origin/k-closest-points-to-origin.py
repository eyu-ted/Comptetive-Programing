class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def myfunct(nums):
            return (nums[0]**2 + nums[1]**2)**0.5
        

        points.sort(key = myfunct)
        print(points)

        return points[:k]
