class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        left_bound = intervals[0][0]
        right_bound = intervals[0][1]

        res = []
        print(intervals)

        for start,end in intervals[1:]:
            if start <= right_bound:
                right_bound = max(end,right_bound)
            else:
                res.append([left_bound,right_bound])
                left_bound = start
                right_bound = end
        
        return res + [[left_bound, right_bound]]