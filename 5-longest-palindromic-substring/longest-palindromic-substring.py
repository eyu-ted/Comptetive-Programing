class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxx = 0
        start = 0

        for i in range(len(s)):
            # odd
            l = r = i
            while l>-1 and r<len(s) and s[l] == s[r]:
                if r-l+1 > maxx:
                    maxx = r-l+1
                    start = l
                l-=1
                r+=1
            # even
            l =i
            r =i+1
            while l>-1 and r<len(s) and s[l] == s[r]:
                if r-l+1 > maxx:
                    maxx = r-l+1
                    start = l
                l-=1
                r+=1
        return s[start:start+maxx]

            
        