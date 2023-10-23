from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Create a Counter for string t to track the characters needed
        t_counter = Counter(t)
        
        # Initialize pointers and variables to keep track of the sliding window
        left, right = 0, 0
        min_len = float('inf')
        min_len_start = 0
        required_chars = len(t)
        
        # Initialize a Counter to track the characters in the current window
        window_counter = Counter()
        
        while right < len(s):
            # Expand the window by moving the right pointer
            if s[right] in t_counter:
                window_counter[s[right]] += 1
                if window_counter[s[right]] <= t_counter[s[right]]:
                    required_chars -= 1
            
            # Check if the window contains all required characters
            while required_chars == 0:
                # Update the minimum window length
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_len_start = left
                
                # Contract the window by moving the left pointer
                if s[left] in t_counter:
                    window_counter[s[left]] -= 1
                    if window_counter[s[left]] < t_counter[s[left]]:
                        required_chars += 1
                left += 1
            
            # Move the right pointer to expand the window
            right += 1
        
        if min_len == float('inf'):
            return ""
        else:
            return s[min_len_start:min_len_start + min_len]

# Example usage
s1 = "ADOBECODEBANC"
t1 = "ABC"
sol = Solution()
print(sol.minWindow(s1, t1))  # Output: "BANC"
