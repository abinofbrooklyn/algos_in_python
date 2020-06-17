from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        queue.append((-1,-1))
        ans = -1
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                ans += 1
                if queue:
                    queue.append((-1,-1))
            else:
                for d in directions:
                    adj_row, adj_col = row + d[0], col + d[1]
                    if ROWS > adj_row >= 0 and COLS > adj_col >= 0:
                        if grid[adj_row][adj_col] == 1:
                             grid[adj_row][adj_col] = 2
                             fresh -= 1
                             queue.append((adj_row, adj_col))
        return ans if fresh == 0 else -1
