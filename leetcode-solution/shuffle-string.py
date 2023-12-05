class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        lis=[""]*len(s)
        for i in range(len(s)):
            lis[indices[i]]=s[i] 
        return "".join(lis)