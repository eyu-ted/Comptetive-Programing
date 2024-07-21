class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        dic =defaultdict(int)
        adj_lis=defaultdict(list)

        for i in range(len(edges)):
            if edges[i] != -1:

                adj_lis[i].append(edges[i])
        

        print(adj_lis)
        maxx =-1
        dp={}
        
        def dfs(node,l):
            nonlocal maxx
        
            dic[node] = l
            if node in dp:
                return dp[node]

            
            for neigh in adj_lis[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    dfs(neigh,l+1)
                else:
                    maxx = max(maxx,l-dic[neigh]+1)
            
            dp[(node)] = maxx
            return maxx
        
        
        for i in range(len(edges)):
            visited =set()
            visited.add(i)
            dfs(i,0)

        return maxx



        