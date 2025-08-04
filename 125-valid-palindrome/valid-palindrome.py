class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        word = ""

        for ch in s:
            if ch.isalnum():
                word += ch.lower()
        
        return word == word[::-1]
        