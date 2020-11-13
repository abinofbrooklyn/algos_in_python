from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        cols = len(matrix[0])
        rows = len(matrix)

        def binary_search(row):
            l, r = 0, cols-1
            while l <= r:
                mid = (l+r)//2
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False

        for row in range(rows):
            if binary_search(row): return True
        False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))
