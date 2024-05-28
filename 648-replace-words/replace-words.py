class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch  in word:
            if ch not in  cur.children:
                cur.children[ch]= TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
    
    def search(self,wrd):
        cur = self.root
        ans = ""
        for ch in wrd:
            ans += ch
            if ch in cur.children:
    
                
                cur = cur.children[ch]
                if cur.is_end == True:
               
                    return ans
                
            else:
                return wrd
        return wrd

    
        
    

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for arr in dictionary:
            self.addWord(arr)
        
        lis = sentence.split()

        res = []
        for wrd in lis:
            res.append(self.search(wrd))
        
        return " ".join(res)


    
    