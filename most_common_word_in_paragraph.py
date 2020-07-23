from typing import List
import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        newParagraph = paragraph.lower()
        for c in string.punctuation:
            newParagraph = newParagraph.replace(c, ' ')

        listOfWords = newParagraph.split(' ')
        dict = {}

        for word in listOfWords:
            if word not in banned and word != '':
                if word in dict:
                    dict[word] += 1
                else:
                    dict[word] = 1

        ans = ""
        best = 0

        for word in dict:
            if dict[word] > best:
                ans = word
                best = dict[word]

        return ans


s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
