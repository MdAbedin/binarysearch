class Solution:
    def solve(self, matrix):
        for r in range(len(matrix)):
            r2 = r
            c = 0
            diagonal = []

            while r2 < len(matrix) and c < len(matrix[0]):
                diagonal.append(matrix[r2][c])
                r2 += 1
                c += 1

            diagonal.sort()

            r2 = r
            c = 0

            while r2 < len(matrix) and c < len(matrix[0]):
                matrix[r2][c] = diagonal[c]
                r2 += 1
                c += 1

        for c in range(len(matrix[0])):
            c2 = c
            r = 0
            diagonal = []

            while r < len(matrix) and c2 < len(matrix[0]):
                diagonal.append(matrix[r][c2])
                r += 1
                c2 += 1

            diagonal.sort()

            c2 = c
            r = 0

            while r < len(matrix) and c2 < len(matrix[0]):
                matrix[r][c2] = diagonal[r]
                r += 1
                c2 += 1

        return matrix
