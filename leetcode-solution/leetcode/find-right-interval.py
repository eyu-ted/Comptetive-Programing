class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic ={}
        nums = [ ]
        for i in range(len(intervals)):
            dic[intervals[i][0]] = i
            nums.append(intervals[i][0])
 
        nums.sort()

        ans = []
        for a ,b in intervals:
            index = bisect_left(nums,b)
            
       

            if index==len(intervals):
                ans.append(-1)
            else:
                ans.append(dic[nums[index]])
        return ans

    
            
        
