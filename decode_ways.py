class Solution:
    def decode_ways(self, s: str) -> int:
        memo = [0] * (len(s) + 1)
        return self.helper(s, len(s), memo)

    def helper(self, s, index, memo):
        if index == 0:
            return 1
        val = len(s) - index
        if s[val] == '0':
            return 0
        if memo[index] != 0:
            return memo[index]
        res = self.helper(s, index-1, memo)
        if index >= 2 and int(s[val:val+2]) <= 26:
            res += self.helper(s, index-2, memo)
        memo[index] = res
        return res
