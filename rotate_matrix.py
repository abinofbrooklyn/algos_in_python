class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(N):
            for j in range(i,N):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        for i in range(N):
            for j in range(N//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][N-1-j]
                matrix[i][N-1-j] = tmp
