class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map=set()
        l=0
        maxx=0
        for r in range(len(s)):
            while map and s[r] in map:
                map.remove(s[l])
                l+=1
            map.add(s[r])
            maxx=max(maxx,len(map))
        return maxx