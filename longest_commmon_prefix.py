class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        prefix_len = len(prefix)

        for s in strs[1:]:
            while prefix != s[0:prefix_len]:
                prefix = prefix[0:(prefix_len-1)]
                prefix_len -= 1

                if prefix_len == 0:
                    return ""

        return prefix

s = Solution()
s.longestCommonPrefix(["flower","flow","flight"])
