class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        ans=0
        for ch in s:
            if ch=="(":
                stack.append(ch)
            else:
                if stack==[]:
                    ans+=1
                elif stack[-1]=="(":
                    stack.pop()
                    continue
        return ans+len(stack)

        

    
        