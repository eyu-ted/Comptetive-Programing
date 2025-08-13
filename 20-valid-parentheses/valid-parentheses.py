class Solution:
    def isValid(self, s: str) -> bool:


        stack = []
        dic = { "(":")", "{":"}" , "[":"]"}

        for ch in s:

            if ch == ")" or ch == "}" or ch == "]":
                if not stack:
                    return False
                last = stack.pop()
                if dic[last] != ch:
                    return False
            else:
                stack.append(ch)
                
        return stack == []
                

        