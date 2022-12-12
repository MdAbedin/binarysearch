class Solution:
    def solve(self, matrix):
        col_counts = [sum(matrix[r][c] for r in range(len(matrix))) for c in range(len(matrix[0]))]
        one_count = sum(cell for row in matrix for cell in row)
        ans = -inf

        for r in range(len(matrix)):
            row_count = sum(cell for cell in matrix[r])

            for c in range(len(matrix[0])):
                ans = max(ans, one_count - row_count + (len(matrix[0])-row_count) - (col_counts[c]-(1 if matrix[r][c] == 1 else -1)) + (len(matrix)-(col_counts[c] - (1 if matrix[r][c] == 1 else -1))))

        return ans
