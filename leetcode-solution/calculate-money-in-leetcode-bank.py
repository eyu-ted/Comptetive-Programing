class Solution:
    def totalMoney(self, n: int) -> int:
        s=28
        l=0
        lis=[1,2,3,4,5,6,7]
        j=0
        if n<7:
            for i in range(1,n+1):

                l+=i
            return l

        
        else:
            for i in range(7,n):
                s=s+lis[j]+1
                lis[j]+=1
                j+=1
                if j==7:
                    j=0
        return s

        