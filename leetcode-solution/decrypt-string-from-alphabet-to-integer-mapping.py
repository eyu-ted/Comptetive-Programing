class Solution:
    def freqAlphabets(self, s: str) -> str:
        res=""
        i=0
        while i<len(s):
            c=i+2
            if c<len(s) and s[c]=="#":
                n=s[i:c]
                res+=chr(int(n)+96)
                i=c
            elif s[i]!="#" :
                res+=chr(int(s[i])+96)
            i+=1
        return res


            



        
        