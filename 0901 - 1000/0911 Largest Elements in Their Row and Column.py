class Solution:
    def solve(self, matrix):
        row_sums = list(map(sum,matrix))
        col_sums = list(map(sum,[[row[c] for row in matrix] for c in range(len(matrix[0]))]))

        return sum(row_sums[r]==1 and col_sums[c]==1 and matrix[r][c]==1 for r in range(len(matrix)) for c in range(len(matrix[0])))
