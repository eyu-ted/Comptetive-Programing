class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        paths = []
        target = len(graph) - 1


        def backtrack(path, node):

            if node == target:
                paths.append(path[:])
                return 
            

            for neighbor in graph[node]:

                path.append(neighbor)
                backtrack(path, neighbor)
                path.pop()
        

        backtrack([0],0)

        return paths