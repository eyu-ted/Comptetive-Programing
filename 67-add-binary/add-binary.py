class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = len(a)-1
        r = len(b)-1
        rem = 0
        result = []
        while l >-1 or r>-1:
            if l>-1:
                num1 = int(a[l])
                l-=1
            else:
                num1 =0
            if r>-1:
                num2 = int(b[r])
                r-=1
            else:
                num2 =0
            
            if num1 + num2 + rem ==2:
                rem = 1
                result.append("0")
            elif num1 + num2 + rem ==3:
                rem = 1
                result.append("1")
            else:
                result.append(str(num1+num2+rem))
                rem = 0
        if rem:
            result.append(str(rem))
        return "".join(result)[::-1]



