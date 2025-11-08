class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        l = 0
        maxx = 0
        for r ,ch in  enumerate(s):

            dic[ch] += 1
            while dic[ch] > 1:
                dic[s[l]] -= 1
                if dic[s[l]] == 0:
                    dic.pop(s[l])
                l+=1
            maxx = max(maxx,r-l+1)
        
        return maxx
            

        