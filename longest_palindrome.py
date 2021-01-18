class Solution:
    def longestPalindrome(self, s: str) -> int:
        matches = 0
        letters = set()

        for c in str:
            if c in letters:
                matches += 1
                letters.remove(c)
            else:
                letters.add(c)

        longest = matches * 2
        if len(letters) != 0:
            longest += 1

        return longest
