from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      dp = [False] * (len(s) + 1)
      dp[0] = True
      for i in range(len(s)):
        for j in range(i,len(s)):
          if dp[i] and s[i:j+1] in wordDict:
            dp[j+1] = True
      return dp[-1]

s = Solution()
print(s.wordBreak("leetcode", ["leet","code"]))
print(s.wordBreak("applepenapple", ["apple", "pen"]))
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
