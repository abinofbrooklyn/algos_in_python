from typing import List
class Solution:
    def minToClimbStairs(self, cost: List[int]) -> int:
        for i in range(2,len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])

s = Solution()
s.minToClimbStairs([[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]])
