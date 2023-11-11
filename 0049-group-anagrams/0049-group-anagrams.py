class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            # Sort the string to use as a key
            key = tuple(sorted(s))
            if key in anagrams:
                anagrams[key].append(s)
            else:
                anagrams[key] = [s]

        return list(anagrams.values())
