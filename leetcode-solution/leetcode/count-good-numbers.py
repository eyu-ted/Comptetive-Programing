
class Solution:
    def myPow(self,x,n,mod):
        
        if n==0:
            return 1
        elif n==1:
            return x

        if n<0:
            return 1/self.myPow(x,abs(n),mod)
        
        val=self.myPow(x,n//2,mod)
        if n%2==0:
            return (val * val) % mod
        else:
            return (x*val*val) % mod


    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        if n%2 == 0:
            fiv = self.myPow(5,n//2,mod)
            four = self.myPow(4,n//2,mod)
        else:
            fiv = self.myPow(5,n//2,mod) * 5
            four = self.myPow(4,n//2,mod)


        return (fiv * four) % mod



        
        



        
            
        