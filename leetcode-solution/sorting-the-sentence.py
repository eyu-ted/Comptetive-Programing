class Solution:
    def sortSentence(self, s: str) -> str:
        lis=s[::-1].split()
        lis.sort()
        ans=[]
        for word in lis:
            ans.append(word[1:][::-1])
        return " ".join(ans)     

        
        