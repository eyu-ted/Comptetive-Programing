class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stack = []

        for ch in s:
            if ch != "#":
                stack.append(ch)
            elif stack:
                stack.pop()
        

        s = "".join(stack)
        stack = []
        for ch in t:
            if ch != "#":
                stack.append(ch)
            elif stack:
                stack.pop()
        
        t = "".join(stack)

        return s ==t

        