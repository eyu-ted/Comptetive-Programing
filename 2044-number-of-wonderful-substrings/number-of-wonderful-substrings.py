class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        n = 0
        count = defaultdict(int)
        count[0] = 1
        ans = 0
        
        for ch in word:
            n ^= 1 <<(ord(ch)-ord('a'))
            ans+=count[n]
            for i in range(10):
                ans+=count[n ^ (1 << i)]
            count[n]+=1
        
        return ans