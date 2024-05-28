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
            if ch not in cur.children :
                cur.children[ch]= TrieNode()
            cur = cur.children[ch]
        cur.is_end = True
    def search(self,wrd):
        cur = self.root
        res = ""
        for ch in wrd:
            
            if ch in cur.children:
                cur = cur.children[ch]
                if cur.is_end != True:
                    return res
                else:
                    res+=ch
            else:
                return ""
        return res
    def longestWord(self, words: List[str]) -> str:
        for arr in words:
            self.addWord(arr)
        
        ans = []
        
        for arr in words:
            x = self.search(arr)
            if x != "":
                if ans == []:
                    ans = [x]
                elif  len(x) > len(ans[0]):
                    ans = [x]
                elif len(x) == len(ans[0]):
                    ans.append(x)

        ans.sort()
        return ans[0] if len(ans)>=1 else ""

        