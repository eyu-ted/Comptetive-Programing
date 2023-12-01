class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alpha = {c: i for i, c in enumerate(order)}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i + 1]
            minn=min(len(word1),len(word2))
            for j in range(minn):
                if word1[j] != word2[j]:
                    if alpha[word1[j]] > alpha[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False

        return True
        