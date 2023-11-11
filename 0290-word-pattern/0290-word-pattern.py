class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            # Check for conflicting mappings
            if (char in char_to_word and char_to_word[char] != word) or \
               (word in word_to_char and word_to_char[word] != char):
                return False

            char_to_word[char] = word
            word_to_char[word] = char

        return True
