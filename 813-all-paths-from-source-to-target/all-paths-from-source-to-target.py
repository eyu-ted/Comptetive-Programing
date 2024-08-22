class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            if node == len(graph) - 1:
                result.append(path)
                return
            
            for next_node in graph[node]:
                dfs(next_node, path + [next_node])
    
        result = []
        dfs(0, [0])
        return result
