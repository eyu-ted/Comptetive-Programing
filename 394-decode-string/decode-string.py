class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        result = ""

        for ch in s:
            
            if ch == "]":
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                num = 0
                power = 0
                while stack and stack[-1].isdigit():
                    n = stack.pop()
                    num += int(n) * 10**power
                    power += 1
                
                
                stack.append(temp * num)
            else:
                stack.append(ch)
        
        if stack:
            result += "".join(stack)
        return result 
        