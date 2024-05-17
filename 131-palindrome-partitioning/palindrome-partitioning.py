class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispal(i,j):
            return s[i:j+1]==s[i:j+1][::-1]

        
        path =[]
        ans =[]
        def dp(i):
            if i>=len(s):
                ans.append(path.copy())
                return 

            for j in range(i,len(s)):
                if ispal(i,j):
                    path.append(s[i:j+1])
                    dp(j+1)
                    path.pop()
                
        dp(0)
        return ans
                
        