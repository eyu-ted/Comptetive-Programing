class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        check=["qwertyuiop","asdfghjkl","zxcvbnm"]
        res=[]
        for word in words:
            if word[0].lower() in check[0]:
                code=check[0]
            elif word[0].lower() in check[1]:
                code=check[1]
            else:
                code=check[2]
            flag=0
            for char in word:
                if char.lower() not in code:
                    flag=1
            if flag==0:
                res.append(word)
        return res

        





        

        