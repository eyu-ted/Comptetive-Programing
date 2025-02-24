class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        left_bound = intervals[0][0]
        right_bound = intervals[0][1]

        res = []
        intervals = intervals[1:]

        for start,end in intervals:
            if start <= right_bound:
                right_bound = max(end,right_bound)
            else:
                res.append([left_bound,right_bound])
                left_bound = start
                right_bound = end
        
        return res + [[left_bound, right_bound]]