      
class Solution:
    def __init__(self):
        self.adj_list = collections.defaultdict(set)
        self.visited = set()
        self.required_rank = 0

    def connect(self, src, dst):
        self.adj_list[src].add(dst)
        self.adj_list[dst].add(src)

    def build(self, edges):
        for edge in edges:
            self.connect(*edge)
        self.required_rank = len(self.adj_list) - 1

    def rank(self, node):
        return len(self.adj_list[node])

    def sorted_nodes(self):
        return sorted(self.adj_list, key=lambda node: len(self.adj_list[node]), reverse=True)

    def ancestor(self, node):
        return min(self.visited & self.adj_list[node], key=lambda node: len(self.adj_list[node]), default=None)

    def process(self):
        possibilities = 1
        for node in self.sorted_nodes():
            self.visited.add(node)
            node_rank = self.rank(node)
            parent = self.ancestor(node)
            if parent is None:
                if node_rank != self.required_rank:
                    return 0
                else:
                    continue
            else:
                parent_rank = self.rank(parent)
                if self.adj_list[node] - (self.adj_list[parent] | {parent}):
                    return 0
                if node_rank == parent_rank:
                    possibilities = 2
        return possibilities

    def checkWays(self, pairs: List[List[int]]) -> int:
        self.build(pairs)
        return self.process()
