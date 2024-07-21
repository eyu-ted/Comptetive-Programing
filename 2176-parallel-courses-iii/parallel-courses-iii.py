class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_lis = defaultdict(list)
 
        count_edge=defaultdict(int)
        for par,child in relations:
            
            adj_lis[par].append(child)
            count_edge[child]+=1

        leaf =deque()
        

        for i in range(1,n+1):
            if count_edge[i] == 0:
                leaf.append(i)

        total_time = [0] * (n + 1)
        for i in range(1, n + 1):
            total_time[i] = time[i - 1]
    
        ans =0
        while leaf:
            new_leaf=deque()
            while leaf:
                popp = leaf.popleft()
                ans = max(ans, total_time[popp])
                for neigh in adj_lis[popp]:
                    total_time[neigh] = max(total_time[neigh], total_time[popp] + time[neigh - 1])
                    count_edge[neigh] -= 1
                    if count_edge[neigh] == 0:
                        new_leaf.append(neigh)
            
            leaf = new_leaf

        
        return ans


            
         