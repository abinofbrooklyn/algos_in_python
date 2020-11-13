class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i, char in enumerate(order):
            dic[char] = i

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    if dic[w1[i]] > dic[w2[i]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True
