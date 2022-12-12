class Solution:
    def solve(self, matrix):
        row_maxes = [max(row) for row in matrix]
        col_maxes = [max([matrix[r][c] for r in range(len(matrix))]) for c in range(len(matrix[0]))]

        return sum(matrix[r][c] == row_maxes[r] == col_maxes[c] for r in range(len(matrix)) for c in range(len(matrix[0])) )
