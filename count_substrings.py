class Solution:
    def countSubstrings(self, s: str) -> int:
      length = count = len(s)

      if not length:
        return count

      for i in range(length-1):
        ## even
        left, right = i, i+1
        while left > -1 and right < length and s[left] == s[right]:
          left -= 1
          right += 1
          count += 1

        ## odd
        left, right = i, i+2
        while left > -1 and right < length and s[left] == s[right]:
          left -= 1
          right += 1
          count += 1

      return count
  
s = Solution()
print(s.countSubstrings("aaa"))
print(s.countSubstrings("abc"))
