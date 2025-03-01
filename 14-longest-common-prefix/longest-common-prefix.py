class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minn = len(strs[0])

        for wrd in strs:
            if len(wrd) < minn:
                minn = len(wrd)
        
        result = 0
        for i in range(minn):
            sett = set()
            for word in strs:
                sett.add(word[i])
            
            if len(sett) != 1:
                return strs[0][:result]
            result += 1
        return strs[0][:result]
        