from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_map = {}  # Dictionary to store the count of each word in words
        result = []

        # Populate the word_map with the count of each word in words
        for word in words:
            if word in word_map:
                word_map[word] += 1
            else:
                word_map[word] = 1

        for i in range(word_len):
            left = i  # Left boundary of the sliding window
            sub_map = {}  # Dictionary to store the count of words in the current window
            count = 0  # Count of words in the current window

            for j in range(i, len(s) - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_map:
                    if word in sub_map:
                        sub_map[word] += 1
                    else:
                        sub_map[word] = 1
                    count += 1

                    while sub_map[word] > word_map[word]:
                        # Move the left boundary of the window
                        left_word = s[left:left + word_len]
                        sub_map[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == word_count:
                        # If all words are found, add the starting index to the result
                        result.append(left)

                else:
                    # Reset the window if an unrecognized word is encountered
                    sub_map = {}
                    count = 0
                    left = j + word_len

        return result
