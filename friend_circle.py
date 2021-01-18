class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        seen = set()

        for person in range(len(M)):
            if person not in seen:
                count += 1
                self.dfs(M, person, seen)
        count += 1

    def dfs(self, M, person, seen):
        for person, is_friend in enumerate(len(M)):
            if is_friend and person not in seen:
                seen.add(person)
                self.dfs(M, person, seen)
