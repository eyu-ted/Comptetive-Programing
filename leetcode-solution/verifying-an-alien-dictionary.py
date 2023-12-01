class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic= {n:i for i,n in enumerate(order)}
        
        for i in range(len(words)-1):
            flag=0
            word1=words[i]
            word2=words[i+1]
            minn= min(len(word1),len(word2))
            for j in range(minn):
            
                if word1[j]!=word2[j]:
                    if dic[word1[j]] > dic[word2[j]]:
                        return False
                    flag=1
                    break
            if flag==0:
                if len(word1)>len(word2):
                    return False
        return True
        