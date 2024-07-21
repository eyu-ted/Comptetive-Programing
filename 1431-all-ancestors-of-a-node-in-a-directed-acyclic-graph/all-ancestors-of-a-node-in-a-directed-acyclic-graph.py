class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        adj_lis = defaultdict(set)

        for par,child in edges:
            adj_lis[child].add(par)
        

        dp ={}

        def dfs(node):

            if node in dp:
                return dp[node]

            ancestor = set(adj_lis[node])

            for par in adj_lis[node]:
                ancestor |= dfs(par) 

                

            dp[node]=ancestor

            return ancestor
        
        ans =[]
        for i in range(n):
            if i not in dp:
                dfs(i)

            ans.append(sorted(list(dp[i])))
        
        # print(dp)
        return ans
