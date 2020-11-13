from typing import List

class Solution:
    def word_subsets(self, A: List[str], B: List[str]) -> List[str]:
        b_count = [0] * 26
        for word in B:
            tmp_count = self.count(word)
            for i in range(0,26):
                b_count[i] = max(b_count[i], tmp_count[i])

        output = []
        for word in A:
            tmp_count = self.count(word)

            universal = True
            for i in range(0,26):
                if tmp_count[i] < b_count[i]:
                    universal = False

            if universal:
                output.append(word)

        return output

    def count(self, word):
        output = [0] * 26
        for letter in word:
            idx = ord(letter) - ord("a")
            output[idx] += 1
        return output



s = Solution()
A = ["amazon","apple","facebook","google","leetcode"]
B = ["e","o"]
print(s.word_subsets(A, B))
