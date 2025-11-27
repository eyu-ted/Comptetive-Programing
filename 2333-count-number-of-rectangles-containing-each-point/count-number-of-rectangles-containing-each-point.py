class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        
        from collections import defaultdict

        dic = defaultdict(list)

        for x,y in rectangles:
            dic[y].append(x)
        
        for key,_ in dic.items():
            dic[key].sort()
        


        result = []

        for x,y in points:
            tot = 0
            for h in range(y,101):
                if dic[h]:
                    tot += ( len(dic[h]) - bisect_left(dic[h], x) )
            result.append(tot)
        return result 