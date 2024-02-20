class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])
            elif s[i]==")":
                if not stack or stack.pop() !="(":
                    return False
            elif s[i]=="]":
                if not stack or stack.pop() !="[":
                    return False
            elif s[i]=="}":
                if not stack or stack.pop() !="{":
                    return False
        return True if not stack else False
                        