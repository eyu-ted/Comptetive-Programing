class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj_list = defaultdict(list)
        for a,b in prerequisites:
            adj_list[b].append(a)
        
        dp ={}
        def dfs(crs):

            if crs in  dp:
                return dp[crs]
            dp[crs]  =set()
            for neigh in adj_list[crs]:
                dp[crs] |= dfs(neigh)
            dp[crs].add(crs)


            return dp[crs]
        
        for i in range(numCourses):
            dfs(i)
        
        ans = []
        for u,v in queries:
            if u in dp[v]:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans

            