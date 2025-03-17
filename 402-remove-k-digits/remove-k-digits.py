class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []

        for ch in num:

            while stack and stack[-1] > ch and k:
                stack.pop()
                k-=1
            
            stack.append(ch)
        
        while k:
            stack.pop()
            k-=1
        i  = 0
        while i < len(stack) and stack[i] == "0":
            i+=1
        print(stack)
        return "".join(stack[i:]) if stack[i:] else "0"

        
        