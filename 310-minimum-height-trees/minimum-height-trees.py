class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
        dic = defaultdict(list)

        for node,neigh in edges:
            dic[node].append(neigh)
            dic[neigh].append(node)
        
        edge_count = {}
        leaves = deque()
        for par,neigh in dic.items():
            if len(neigh) ==1:
                leaves.append(par)
            
            edge_count[par] = len(neigh)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            
            for i in range(len(leaves)):
                node = leaves.popleft()
                n-=1
                for neigh in dic[node]:
                    edge_count[neigh]-=1
                    if edge_count[neigh] ==1:
                        leaves.append(neigh)
          