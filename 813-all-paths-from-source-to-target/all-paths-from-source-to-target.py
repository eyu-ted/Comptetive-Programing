class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        mapper = defaultdict(int)
        for i in range(len(graph)):
            mapper[i] = graph[i]

        result = []
        def dfs(node,path):

            if node == len(graph)-1:
                
                result.append(path.copy())
                return



            for neigh in mapper[node]:
                path.append(neigh)
                dfs(neigh,path)
                path.pop()
        
        dfs(0,[0])

        return result
                


            


        