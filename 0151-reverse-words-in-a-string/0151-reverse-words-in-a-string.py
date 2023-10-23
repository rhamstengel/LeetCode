class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words
        words = s.split()
        
        # Reverse the order of the words
        words.reverse()
        
        # Join the reversed words with a single space separator
        return ' '.join(words)
