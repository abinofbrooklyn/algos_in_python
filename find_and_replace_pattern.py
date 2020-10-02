class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matches = []
        for word in words:
            if self.align(word,pattern):
                matches.append(word)
        return matches

    def align(self, word, pattern):
        if len(word) != len(patter):
            return False

        word_to_pattern = [0] * 256
        pattern_to_word = [0] * 256

        for i in range(0, len(word)):
            word_char = ord(word[i])
            pattern_char = ord(pattern[i])

            if word_to_pattern[word_char] == 0:
                word_to_pattern[word_char] = pattern_char
            if pattern_to_word[pattern_char] == 0:
                pattern_to_word[pattern_char] = word_char
            if (word_to_pattern[word_char] != pattern_char or pattern_to_word[pattern_char] != word_char):
                return False
        return True

s = Solution()
s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")
