class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        bitmask = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        result = 0
        
        for char in word:
            bitmask ^= 1 << (ord(char) - ord('a'))
            result += prefix_count[bitmask]
  
            for i in range(10):
                result += prefix_count[bitmask ^ (1 << i)]
                

            prefix_count[bitmask] += 1
        
        return result