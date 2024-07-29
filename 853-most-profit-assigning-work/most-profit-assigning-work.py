class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        worker.sort()
        ans =0
        
        maxx = 0
        temp =[]
        for i in range(len(difficulty)):
            temp.append([difficulty[i],profit[i]])
        temp.sort()
        i=0
        for num in worker:
            while i< len(difficulty) and num >= temp[i][0]:
                maxx = max(maxx,temp[i][1])
                i+=1
            
            ans += maxx 

        return ans
            


