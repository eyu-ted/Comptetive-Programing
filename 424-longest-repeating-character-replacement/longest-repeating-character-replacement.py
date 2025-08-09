class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l= 0
        dic = defaultdict(int)
        maxx_tol = 0
        ans = 0
        for r in range(len(s)):
            dic[s[r]] += 1
            maxx_tol = max(maxx_tol,dic[s[r]])
            
            while r-l+1 - maxx_tol > k:
                dic[s[l]] -= 1
                l+=1

            ans = max(ans , r-l+1)
        return ans
                
        


            




        