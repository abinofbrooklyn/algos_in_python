class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        for c in s:
            if c not in hash:
                hash[c] = 1
            else:
                hash[c] += 1

        for i, c in enumerate(s):
            val = hash[c]
            if val == 1:
                return i
        return -1
            
