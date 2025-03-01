class Solution:
    def equalFrequency(self, word: str) -> bool:

        count = defaultdict(int)

        for char in word:
            count[char] += 1
        
        maxx = max(count.values())
        minn = min(count.values())

        for ch in word:
            if count[ch] == maxx:
                count[ch] -= 1
                if not count[ch]:
                    count.pop(ch)
                break
    
        lis = list(count.values())

        count[ch] += 1
    
        for ch in word:
            if count[ch] == minn:
                count[ch] -= 1
                if not count[ch]:
                    count.pop(ch)
                break
        lis1 = count.values()
    
        return len(set(lis)) == 1 or len(set(lis1)) == 1 