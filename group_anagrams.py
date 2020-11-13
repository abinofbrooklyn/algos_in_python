from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        return anagrams.values()

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
