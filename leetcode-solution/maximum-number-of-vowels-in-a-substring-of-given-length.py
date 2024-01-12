class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=({"a","e","i","o","u"})
        l=0
        count=0
        maxx=0
        for r in range(len(s)):
            if s[r] in vowels:
                count+=1
            if r>=k:
                if s[l] in vowels:
                    count-=1
                l+=1
            maxx=max(maxx,count)
        return maxx
            

        