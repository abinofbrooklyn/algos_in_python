class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, result = 0, 0
        for c in s:
            count += 1 if c == 'L' else -1
            if count == 0:
                result += 1
        return result 
