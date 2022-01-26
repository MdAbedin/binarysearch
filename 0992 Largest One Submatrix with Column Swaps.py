class Solution:
    def solve(self, matrix):
        if not matrix or not matrix[0]: return 0

        R,C = len(matrix),len(matrix[0])

        for c in range(C):
            for r in range(1,R):
                if matrix[r][c] == 1: matrix[r][c] += matrix[r-1][c]

        for row in matrix: row.sort(reverse = True)

        return max((i+1)*num for row in matrix for i,num in enumerate(row))
