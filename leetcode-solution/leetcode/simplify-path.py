class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        lis=path.split("/")
        print(lis)

        for i in range(len(lis)):
            if lis[i]=="." or lis[i]=="/":
                continue
            elif stack and lis[i]=="..":
                stack.pop()
            elif lis[i]!="" and lis[i]!="..":
                stack.append(lis[i])
        word=[]
        for i in range(len(stack)):
            word.append("/")
            word.append(stack[i])
        print(word)

        return "/" if len(word)==0 else "".join(word)
        