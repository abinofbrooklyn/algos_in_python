class Solution:
    def rotate_matrix(self, matrix):
        size = len(matrix) - 1

        for row in range(0, len(matrix) // 2):
            for col in range(row, size - row):
                top = matrix[row][col]
                left = matrix[size-col][row]
                bottom = maxtrix[size-row][size-col]
                right = matrix[col][size-row]

                matrix[row][col] = left
                matrix[size-row][row] = bottom
                matrix[size-row][size-col] = right
                matrix[col][size-row] = top
        return matrix
