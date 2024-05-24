class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch  in word:
            indx = ord(ch)-97
            if cur.children[indx] == None:
                cur.children[indx]= TrieNode()
            cur = cur.children[indx]
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(i,cur):
            if i== len(word):
                return cur.is_end
            if word[i] ==".":
                for nex in cur.children:
                    if nex and dfs(i+1,nex):
                        return True
                return False
                
            else:
                indx= ord(word[i])-97
                if not cur.children[indx]:
                    return False
                return dfs(i+1,cur.children[indx])
                
        curr = self.root
        return dfs(0,curr)
            
            
            

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)