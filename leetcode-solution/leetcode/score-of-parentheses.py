class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for ch in s:
            if ch=="(":
                stack.append(ch)
                t=0
            else:
                x=stack.pop()
                if x=="(":
                    t+=1
                    stack.append(t)
                else:
                    while stack and stack[-1]!="(":
                        x=x+stack.pop()
                    stack.pop()
                    stack.append(2*x)
        print(stack)
        return sum(stack)
                    

            



        