class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for n in tokens:
            if n=="/":
                x,y=stack.pop(),stack.pop()
                stack.append(int(y/x))
            elif n=="*":
                stack.append(stack.pop()*stack.pop())
            elif n=="-":
                x,y=stack.pop(),stack.pop()
                stack.append(y-x)
            elif n=="+":
                stack.append(stack.pop()+stack.pop())
            else:
                stack.append(int(n))
        return int(stack[0])
        