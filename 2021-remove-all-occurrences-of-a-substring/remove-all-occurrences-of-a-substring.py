class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:


        stack = [ ]

        for ch in s:
            stack.append(ch)

            if len(stack) >= len(part):

                flag = True
                i= len(stack)-len(part)
                j = 0
                while i < len(stack):
                    if stack[i] != part[j]:
                        flag = False
                        break
                    i+=1
                    j+=1
                
                if flag:
                    for _ in range(len(part)):
                        stack.pop()
            
            

        print(stack)
        return "".join(stack)



        


        