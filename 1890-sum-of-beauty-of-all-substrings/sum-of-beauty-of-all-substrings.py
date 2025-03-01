class Solution:
    def beautySum(self, s: str) -> int:

        
        ans = 0
        for i in range(len(s)):
            count = defaultdict(int)
            word = s[i:]
            for ch in word:
                count[ch] += 1  
                ans += max(count.values()) - min(count.values())

                
        return ans