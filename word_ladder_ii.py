import collections
from typing import List

class Solution:
    def findLadders(self, begin_word: str, end_word: str, word_list: List[str]) -> List[List[str]]:
        def dfs(word):
            if word == end_word:
                res.append(list(tmp))
                return
            if word in graph:
                for nei in graph[word]:
                    if dist[nei] == dist[word]-1:
                        tmp.append(nei)
                        dfs(nei)
                        tmp.pop()

        word_set = set(word_list)
        if end_word not in word_set:
            return []
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        q = collections.deque([(end_word, 0)])
        min_dist = float('inf')
        seen = set([end_word])
        graph = collections.defaultdict(set)
        dist = {}

        while q:
            word, d = q.popleft()
            dist[word] = d
            for i in range(len(word)):
                for alpha in alphabets:
                    new = word[:i]+alpha+word[i+1:]
                    if new == begin_word:
                        if min_dist > d + 1:
                            min_dist = d + 1
                        graph[begin_word].add(word)
                    else:
                        if new in word_set:
                            graph[word].add(new)
                            graph[new].add(word)
                            if new not in seen:
                                seen.add(new)
                                q.append((new, d + 1))

        if min_dist == float('inf'): return []
        res = []
        tmp = [begin_word]

        for nei in graph[begin_word]:
            if dist[nei] == min_dist - 1:
                tmp.append(nei)
                dfs(nei)
                tmp.pop()

        return res
