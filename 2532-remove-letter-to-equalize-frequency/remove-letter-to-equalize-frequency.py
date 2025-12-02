class Solution:
    def equalFrequency(self, word: str) -> bool:
        if word.count(word[0]) == len(word):
            return True
        freq_count = Counter(Counter(word).values())
        
        if len(freq_count) == 1: 
            # check if either every char occured only once 1 in freq_count OR  if all the characters are similar or duplicates 1 in _freq_count.values()
            return 1 in freq_count 
        
        elif len(freq_count) == 2: 

            return freq_count[1] == 1 or freq_count[min(freq_count) + 1] == 1 
        return False 