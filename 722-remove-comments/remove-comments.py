class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        st = ""
        ans = []
        flag = False

        for element in source:
            i= 0

            while i<len(element):


                ch = element[i:i+2]

                if ch == "/*" and not flag:
                    flag = True
                    i+=2
                elif ch == "*/" and flag:
                    flag = False
                    i+=2
                elif ch == "//" and not flag:
                    break
                elif ch == "//" and flag :
                    i+=2
                else:
                    if not flag:
                        st += element[i]
                    i+=1
            
            if st and not flag:
                ans.append(st)
                st= ""

        return ans



        