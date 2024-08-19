class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count =0
        stack = [[s[0],1]]
        for i in range(1,len(s)):
            if stack and s[i] == stack[-1][0]:
                stack.append([s[i],stack[-1][1]+1])
            else:
                stack.append([s[i],1])
            if stack[-1][1] ==k:
                c=k
                while c:
                    stack.pop()
                    c-=1
        ans =[]
        for ch,count in stack:
            ans.append(ch)
        return "".join(ans)
    


        