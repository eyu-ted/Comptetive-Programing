class Solution:
    def isHappy(self, n: int) -> bool:
        dic={}
        while True:
            if n in dic:
                return False
            else:
                dic[n]=0
            sum=0
            for i in str(n):
                sum+=int(i)**2
                n=sum
            if sum==1:
                return True


        