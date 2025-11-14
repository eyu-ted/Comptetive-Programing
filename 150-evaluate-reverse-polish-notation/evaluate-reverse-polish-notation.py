class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        result = 0
        opp = {"+","-","*","/"}
        for ch in tokens:

            if ch in opp:
                num1 = stack.pop()
                num2 = stack.pop()
                if ch == "+":
                    temp = (num1+num2)
                elif ch =="*":
                    temp = (num1*num2)
                elif ch == "-":
                    temp = (num2-num1)
                else:
                    if num2/num1 < 0:
                        temp = -1*int(abs(num2/num1))
                    else:
                        temp = num2//num1


                    
                stack.append(temp)
            else:
                stack.append(int(ch))
        
            

        return stack[0]
