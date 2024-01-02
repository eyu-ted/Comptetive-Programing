class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point):
            x=point[0]
            y=point[1]
            return (x**2+y**2)**0.5
        points.sort(key=distance)
        return points[:k]
        

        
        