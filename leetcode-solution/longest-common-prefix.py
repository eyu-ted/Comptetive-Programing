class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        l=len(strs[0])
        for i in range(l):
            for s in strs:
                if i==len(s)or s[i]!=strs[0][i]:
                    return ans
            ans+=strs[0][i]
        return ans

        
        
        