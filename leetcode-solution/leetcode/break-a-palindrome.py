class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        lis=[]
        c=palindrome.count("a")
        for ch in palindrome:
            lis.append(ch)
        if len(palindrome)==1:
            return ""
        elif c ==len(palindrome):
            lis[-1]="b"
            return "".join(lis)

        else:
            
            for i,ch in enumerate(lis):
                if ch!="a":
                    if i != len(lis)//2:
                        lis[i]="a"
                    else:
                        lis[-1]="b"
                    return "".join(lis)

                    