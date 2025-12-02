class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        dic = Counter(s)
        dic1 = Counter(t)

        ans = 0
        for key in dic:

            ans += max(0,dic[key] - dic1[key])
        
        return ans

            