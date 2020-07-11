from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            dict[tuple(sorted(s))] = dict.get(tuple(sorted(s)),[]) + [s]
        return [sorted(item) for item in dict.values()]

s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
