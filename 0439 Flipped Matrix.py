class Solution:
    def solve(self, matrix):
        R,C = len(matrix), len(matrix[0])

        for r in range(R):
            if matrix[r][0] == 0:
                matrix[r] = [1-bit for bit in matrix[r]]

        for c in range(C):
            if sum(row[c] == 0 for row in matrix) > R/2:
                for r in range(R):
                    matrix[r][c] = 1-matrix[r][c]

        return sum(int("".join(map(str, row)), 2) for row in matrix)
