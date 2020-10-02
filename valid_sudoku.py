class Solution:
    def validSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(0,9):
            for col in range(0,9):
                if board[row][col] != ".":
                    val = board[row][col]
                    if (row,val) in seen or (val, col) in seen or (row//3, col//3, val) in seen:
                        return False
                    seen.add((row,val))
                    seen.add((val, col))
                    see.add((row//3, col//3, val))
        return True
 
