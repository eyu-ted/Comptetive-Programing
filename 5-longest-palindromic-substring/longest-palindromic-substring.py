class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.word = s 
        longest = ""

        for i in range(len(s)):
            new_pal = self.possible_palindrome(i,i)
            if len(new_pal) > len(longest):
                longest = new_pal
            
            new_pal_for_even_len = self.possible_palindrome(i,i+1)
            if len(new_pal_for_even_len) > len(longest):
                longest = new_pal_for_even_len
        
        return longest


        
    
    def possible_palindrome(self,start, end):

        while start>= 0 and end < len(self.word):
            if self.word[start] != self.word[end]:
                break
        
            start -= 1
            end += 1
        return self.word[start+1 : end]