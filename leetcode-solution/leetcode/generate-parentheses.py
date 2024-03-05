class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []

        ans = []

        def backtrack(openP , closeP):

            if openP==closeP==n:
                ans.append("".join(path))
                return 
            
            if openP<n:
                path.append("(")
                backtrack(openP+1 , closeP)
                path.pop()
            if closeP<openP:
                path.append(")")
                backtrack(openP, closeP+1)
                path.pop()
            
        backtrack(0 , 0)

        return ans        