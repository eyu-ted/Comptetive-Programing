class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        stack = [[s[0],1]]

        for ch in s[1:]:
            count = stack[-1][1]
            if count == k:
                while stack and count:
                    stack.pop()
                    count -=1


            if stack and stack[-1][0] == ch:
                stack.append([ch,stack[-1][1]+1])
            else:
                stack.append([ch,1])
        # print(stack)
        count = stack[-1][1]
        if count == k:
                while stack and count:
                    stack.pop()
                    count -=1
        result = ""
        for lis in stack:
            result += lis[0]
        return result