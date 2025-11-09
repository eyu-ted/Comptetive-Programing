class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sett = set(jewels)
        count = 0
        for ch in stones:
            if ch in sett:
                count += 1

        return count 
        