class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dic = {}
        dic[1]  = 0
        def dp(num):
            if num in dic:
                return dic[num]
            
            if num %2 == 0:
                val = 1 + dp(num//2)
            else:
                val = 1 + dp((num * 3) + 1)
            
            dic[num] = val
            return dic[num]
            
        lis = []

        for x in range(lo, hi+1):
            count = dp(x)
            lis.append([count,x])

            
        
        lis.sort()

        return lis[k-1][1]
            

        