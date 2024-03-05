class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n,k):
            if n==1:
                return 0
            prev=helper(n-1 , ceil(k/2))


            if prev==0 and k%2!=0:
                return 0
            elif prev==0 and k%2==0:
                return 1
            elif prev==1 and k%2!=0:
                return 1
            else:
                return 0
        
        
        ans=helper(n,k)
        return ans
        
        




            
