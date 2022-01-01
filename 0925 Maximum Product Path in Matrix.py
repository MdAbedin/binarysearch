class Solution:
    def solve(self, matrix):
        R,C = len(matrix),len(matrix[0])
        matrix[0][0] = [matrix[0][0],matrix[0][0]]

        for r in range(R):
            for c in range(C):
                if [r,c] == [0,0]: continue

                max_,min_ = -inf,inf
                cur = matrix[r][c]

                if r-1 >= 0:
                    max_ = max(max_, matrix[r-1][c][0]*cur, matrix[r-1][c][1]*cur)
                    min_ = min(min_, matrix[r-1][c][0]*cur, matrix[r-1][c][1]*cur)
                if c-1 >= 0:
                    max_ = max(max_, matrix[r][c-1][0]*cur, matrix[r][c-1][1]*cur)
                    min_ = min(min_, matrix[r][c-1][0]*cur, matrix[r][c-1][1]*cur)

                matrix[r][c] = [max_,min_]

        return -1 if matrix[-1][-1][0] < 0 else matrix[-1][-1][0] % (10**9+7)
