class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        dic = defaultdict(int)

        l = 0 
        maxx =0
        
        for r in range(len(s)):

            while l < r and dic[s[r]] > 0:
                dic[s[l]] -= 1
                l += 1 
        
            dic[s[r]] += 1
            maxx = max(maxx,r-l+1)
        return maxx
        

        