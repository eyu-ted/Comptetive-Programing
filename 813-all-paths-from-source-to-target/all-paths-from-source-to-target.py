class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        answer = set()
        def dfs(node, path):
            if node == len(graph)-1:
                answer.add(tuple(path))
                return
            
            for nei in graph[node]:
                dfs(nei, path+[nei])
                
        dfs(0, [0])
        return [list(x) for x in answer]

