class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size+1))
        self.rank = [1]*(size+1)
        self.components = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.components -= 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice=UnionFind(n)
        bob=UnionFind(n)
        edges_needed = 0

        for edge in edges:
            if edge[0] == 3:
                if alice.union(edge[1],edge[2]):
                    bob.union(edge[1],edge[2])
                    edges_needed += 1
        
        for edge in edges:
            if edge[0] == 1:
                if alice.union(edge[1],edge[2]):
                    edges_needed += 1
        

        for edge in edges:
            if edge[0] == 2:
                if bob.union(edge[1], edge[2]):
                    edges_needed += 1

        # print(alice.components )
        # print(bob.components)
        if alice.components >1 or bob.components > 1:
            return -1

        return len(edges)-edges_needed
