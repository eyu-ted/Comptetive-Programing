class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue=deque(tickets)
        value=tickets[k]
        time=0
        while value>0:
            time+=1
            p=queue.popleft()
            if p!=1:
                queue.append(p-1)
            k-=1
            if k==-1:
                k=len(queue)-1
                value-=1


        return time




        # for i in range(len(tickets)):
        #     temp=tickets[i]
        #     tickets[i]=[i,temp]
        # ans=0

        # while True:
        #     i,t=tickets.pop(0)
        #     ans+=1
        #     if i==k and t-1==0:
        #         return ans
        #     if t-1>0:
        #         tickets.append([i,t-1])
        
        