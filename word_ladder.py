from collections import defaultdict
class Solution(object):

    def ladder_length(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        adj = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                adj[word[:i] + '-' + word[i+1:]].append(word)
        visited = set()
        q = collections.deque([(beginWord, 1)])
        while q:
            word, k = q.popleft()
            if word not in visited:
                visited.add(word)
                for i in range(len(word)):
                    neighbors = word[:i] + '_' + word[i+1:]
                    for neighbor in adj[neighbors]:
                        if neighbor not in visited:
                            if neighbor == endWord:
                                return k+1
                            q.append((neighbor, k+1))
        return 0
