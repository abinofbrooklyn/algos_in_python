class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(1,n):
            s = self.count_up(s)
        return s

    def count_up(self, s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while s[i] == s[i+1] and i + 1 < len(s):
                count += 1
                i += 1
            result.append(str(count) + s[i])
            i += 1
        "".join(result)
