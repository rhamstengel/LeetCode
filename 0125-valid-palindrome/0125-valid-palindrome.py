class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        # Check if the modified string is equal to its reverse
        return s == s[::-1]
