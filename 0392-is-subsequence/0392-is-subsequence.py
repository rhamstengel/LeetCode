class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Initialize pointers i and j to the start of s and t, respectively
        i, j = 0, 0
        
        # Loop through t until we reach the end of either s or t
        while i < len(s) and j < len(t):
            # If the current character of s matches the current character of t,
            # move the s pointer to the next character
            if s[i] == t[j]:
                i += 1
            
            # Move the t pointer to the next character
            j += 1
        
        # If we reached the end of s, then s is a subsequence of t
        return i == len(s)
