class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i in range(len(tasks)):
            tasks[i].append(i)

        heapq.heapify(tasks)
        time = tasks[0][0]

        availble =[]

        result = []
        while tasks:
            
            while tasks and tasks[0][0] <= time:
                enq,pt,indx = heapq.heappop(tasks)
                heapq.heappush(availble, [pt,indx])
            if availble:
                pt,indx = heapq.heappop(availble)
                time += pt
                result.append(indx)
            else:
                
                time = tasks[0][0]
        while availble:
            pt,indx = heapq.heappop(availble)
            result.append(indx)
        return result


        


        