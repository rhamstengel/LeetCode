class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        char_index = {}  # A dictionary to store the index of each character.
        max_length = 0  # Initialize the maximum length.
        start = 0  # The start index of the current substring.
        
        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                # If the character is already in the substring, update the start index.
                start = char_index[s[end]] + 1
            char_index[s[end]] = end  # Update the index of the character.
            max_length = max(max_length, end - start + 1)  # Update the maximum length.
        
        return max_length
