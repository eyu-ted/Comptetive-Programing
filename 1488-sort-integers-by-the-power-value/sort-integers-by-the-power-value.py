class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(num):
            count = 0
            temp = num
            while temp != 1:
                if temp % 2 == 0:
                    temp //= 2
                else:
                    temp = (3*temp + 1)
                count +=1
            
            return count
        
        result = []

        for nu in range(lo,hi+1):
            result.append((power(nu), nu))

        result.sort()

        return result[k-1][1] 
