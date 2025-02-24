class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        power = []
        lis = []

        for x in range(lo, hi+1):
            count = 0
            num = x
            while num > 1:
                if num % 2 == 0:
                    num //= 2
                else:
                    num = 3 * num + 1
                count += 1
            
            lis.append([count,x])

            
        
        lis.sort()

        return lis[k-1][1]
            

        