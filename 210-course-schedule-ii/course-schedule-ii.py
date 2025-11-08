class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        dic = defaultdict(list)
        indgree = defaultdict(int)
        
        for a,b in prerequisites:
            dic[b].append(a)
            indgree[a]+=1
        
        q = deque()
        # visited = set()
        result = []
        for i in range(numCourses):
            if i not in indgree:
                q.append(i)
                
                result.append(i)

        
        while q:
            node = q.popleft()

            for neigh in dic[node]:
                indgree[neigh] -=1
                if indgree[neigh] == 0 :
                    q.append(neigh)
                    result.append(neigh)
                    # visited.add(neigh)
        

                

        return result if len(result) == numCourses else []