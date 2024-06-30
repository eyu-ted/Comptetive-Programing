class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        temp=""
        for c in s:
            if c==")":
                while stack[-1]!="(":
                    temp+=stack.pop()
                stack.pop()
                for ch in temp:
                    stack.append(ch)
                temp=""
            else:
                stack.append(c)
        return "".join(stack)
        