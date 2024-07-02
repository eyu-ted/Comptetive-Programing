class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                    rank[rootX] += rank[rootY]
                else:
                    parent[rootX] = rootY
                    rank[rootY] += rank[rootX]
        
  
        for a, b in edges:
            union(a, b)
        
        dic = defaultdict(int)
        for i in range(n):
            root = find(i)
            dic[root] += 1
        
     
        total = n * (n - 1) // 2
        for val in dic.values():
            total -= val * (val - 1) // 2
        
        return total

