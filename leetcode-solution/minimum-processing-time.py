class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        index=0
        maxx=float("-inf")
        for n in processorTime:
            count=0
            while count<4:
                maxx=max(maxx,n+tasks[index])
                index+=1
                count+=1
        return maxx

        

        