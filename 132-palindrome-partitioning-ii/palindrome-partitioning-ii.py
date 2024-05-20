class Solution:
    def minCut(self, s: str) -> int:

        def ispal(i,j):
            return s[i:j+1]==s[i:j+1][::-1]

        dic ={}
        def dfs(i):
            if i>=len(s):
                return 0
            
            path = []
            if i in dic:
                return dic[i]


            for j in range(i,len(s)):
                if ispal(i,j):
                    path.append(1+dfs(j+1))
            print(path)
            if path:
                dic[i] = min(path)
            else:
                dic[i]=0

            return dic[i]
       
        
                
        return dfs(0)-1
        