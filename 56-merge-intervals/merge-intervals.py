class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        result = []
        intervals.sort()

        for start , end in intervals:

            if not result:
                result.append([start, end])
            else:
                if result[-1][1] >= start:
                    result[-1][1] = max(result[-1][1],end)
                else:
                    result.append([start,end])
        
        return result