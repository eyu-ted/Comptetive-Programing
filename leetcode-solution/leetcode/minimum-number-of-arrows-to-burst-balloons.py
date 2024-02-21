class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        minn=float("-inf")
        ans=0
        print(points)
        for arr in points:

            if minn<arr[0]:
                ans+=1
                minn=arr[1]
            else:
                minn=min(minn,arr[1])

        return ans


        