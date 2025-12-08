class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        

        dic = {}

        for i , ch in enumerate(order):
            dic[ch] = i
        
        new_word = []

        for word in words:
            temp = []
            for ch in word:
                temp.append(dic[ch])
            new_word.append(temp)
        
        return sorted(new_word) == new_word

      

        