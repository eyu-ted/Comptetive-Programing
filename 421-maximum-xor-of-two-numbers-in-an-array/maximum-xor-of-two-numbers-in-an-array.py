class TrieNode:
    def __init__(self):
        self.children = [None] * 2
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self,n):
        
        cur = self.root
        bi = 1 << 31  
        
        while bi > 0:
            nu = (n & bi) != 0 
            if not cur.children[nu]:
                cur.children[nu] = TrieNode()
            cur = cur.children[nu]
            bi >>= 1
    
    def search(self,numm):
        cur = self.root
        bi = 1 << 31  
        x = 0 
        path = []
        while bi > 0:
            nu = (numm & bi) != 0  
       
            if cur.children[1 - nu]:
                cur = cur.children[1 - nu]
                path.append(1 - nu)
            else:
                cur = cur.children[nu]
                path.append(nu)
            bi >>= 1
        for i in range(31,-1,-1):
            if path[31-i]==1:
                x += ((2**i))
  
        return x 



        
    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.addWord(num)
        
        maxx = float("-inf")
 
        for num in nums:

            maxx = max(maxx,self.search(num) ^ num)
        
        return maxx

    