class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lookup = {}
        for i, r in enumerate(list1):
            lookup[r] = i

        res = []
        min_sum = float('inf')

        for j, s in enumerate(list2):
            if s in lookup:
                if lookup[s] + j < min_sum:
                    res = [s]
                    min_sum = lookup[s] + j
                elif lookup[s] + j == min_sum:
                    res.append(s)

        return res 
