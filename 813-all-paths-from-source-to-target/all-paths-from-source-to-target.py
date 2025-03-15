class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        answer = []
        def dfs(node ):
            if node == len(graph)-1:
                answer.append(path[:])
                return
            
            for nei in graph[node]:
                path.append(nei)
                dfs(nei)
                path.pop()

        path = [0]      
        dfs(0)
        return [list(x) for x in answer]

