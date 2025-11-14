class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        
        from collections import defaultdict

        dic = defaultdict(list)

        for x,y in rectangles:
            dic[y].append(x)
        for x,y in rectangles:
            dic[y].sort()
        
        result = []
        for x,y in points:
            count = 0
            for h in range(y,101):

                count += len(dic[h]) - bisect_left(dic[h],x)
            
            result.append(count)
        
        return result

            