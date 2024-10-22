class Solution:
    def countVowels(self, word: str) -> int:
        

        vowel = ("a","e","i","o","u")

        v =0
        c =0
        ans =0

        for i,ch in enumerate(word):
            if ch in vowel:
                ans += ((c+1)*(len(word)-i))

            c+=1
                
                
        return ans