import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        res, hash_map = [], Counter(S)
        pq = [(-value,key) for key, value in hash_map.items()]
        heapq.heapify(pq)
        previous_count, previous_letter = 0, ''
        while pq:
          count, letter = heapq.heappop(pq)
          res.append(letter)
          if previous_count < 0:
            heapq.heappush(pq, (previous_count, previous_letter))
          count += 1
          previous_count, previous_letter = count, letter
        res = ''.join(res)
        if len(res) != len(S):
          return ""
        return res

s = Solution()
print(s.reorganizeString("aab"))
print(s.reorganizeString("aaab"))
