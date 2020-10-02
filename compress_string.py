from typing import List

class Solution:
     def compress(self, chars: List[str]) -> int:
        left = i = 0
        while i < len(chars):
            while i < len(chars) and chars[i] == chars[left]:
                i += 1
            if i - left == 1:
                left = i
            else:
                chars[left+1:i] = str(i - left)
                left = left + 2
                i = left

s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))
print(s.compress(["a","b","c"]))
