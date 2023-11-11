class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to count the frequency of each letter in magazine
        letter_count = {}
        for letter in magazine:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        # Check each letter in ransomNote
        for letter in ransomNote:
            if letter not in letter_count or letter_count[letter] == 0:
                # If the letter is not in magazine or has been used up, return False
                return False
            letter_count[letter] -= 1

        # If all letters in ransomNote are found in magazine, return True
        return True
