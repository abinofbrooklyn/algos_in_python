class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = even = 0

        for c in position:
            if c % 2:
                even += 1
            else:
                odd += 1
        return min(even, odd)
        
