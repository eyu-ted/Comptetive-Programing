class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lis =list(s)
        for i in range(0,len(lis),2*k):
            lis[i:i+k]=reversed(lis[i:i+k])
        return "".join(lis)
        