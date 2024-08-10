class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u]) 
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        edgeList.sort(key=lambda x: x[2])
        queries = [(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)]
        queries.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        result = [False] * len(queries)
        edgeIndex = 0


        for p, q, limit, i in queries:
            while edgeIndex < len(edgeList) and edgeList[edgeIndex][2] < limit:
                uf.union(edgeList[edgeIndex][0], edgeList[edgeIndex][1])
                edgeIndex += 1

            if uf.find(p) == uf.find(q):
                result[i] = True
        
        return result

