from typing import List
from itertools import product

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # Create a mapping of the allowed patterns for quick lookup
        self.pattern_map = {}
        for pattern in allowed:
            if pattern[:2] not in self.pattern_map:
                self.pattern_map[pattern[:2]] = []
            self.pattern_map[pattern[:2]].append(pattern[2])
        
        # Recursive function to try building the pyramid
        def build(level):
            if len(level) == 1:
                return True
            next_level = []
            for i in range(len(level) - 1):
                if level[i:i+2] not in self.pattern_map:
                    return False
                next_level.append(self.pattern_map[level[i:i+2]])
            
            # Generate all possible configurations for the next level
            for config in product(*next_level):
                if build("".join(config)):
                    return True
            return False
        
        return build(bottom)

# Test with the provided examples
solution = Solution()
example1_result = solution.pyramidTransition("BCD", ["BCC","CDE","CEA","FFF"])
example2_result = solution.pyramidTransition("AAAA", ["AAB","AAC","BCD","BBE","DEF"])

example1_result, example2_result
