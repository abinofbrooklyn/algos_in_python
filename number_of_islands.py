class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if grid[row][column] == '1':
                    islands += 1
                    self.island(grid, row, column)
        return islands

    def island(self, grid, row, colunm):
        if row < 0 or column < 0 || row == len(grid) || gird[row][column] == '0':
            return
        else:
            grid[row][column] = '0'
            self.island(grid, row, column+1)
            self.island(grid, row, column-1)
            self.island(grid, row+1, column)
            self.island(grid, row-1, column)
