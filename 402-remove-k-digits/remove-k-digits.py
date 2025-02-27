class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        digits = list(num)

        stack = []

        for num in digits:

            while stack and k and stack[-1] > num:
                stack.pop()
                k-=1
            
            stack.append(num)

        if k:
            while k:
                stack.pop()
                k-=1

  
        i = 0
        while i<len(stack) and stack[i] == "0":
            i += 1
        if not stack[i:]:
            return "0"

            
        result = "".join(stack[i:])

        return result

      
