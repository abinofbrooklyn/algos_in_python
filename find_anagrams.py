from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result_list = []
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)-1])

        for i in range(len(p)-1, len(s)):
            s_counter[s[i]] += 1
            if s_counter == p_counter:
                result_list.append(i - len(p)+1)
            s_counter[s[i - len(p)+1]] -= 1
            if s_counter[s[i - len(p)+1]] == 0:
                del s_counter[s[i - len(p)+1]]
        return result_list
