class Solution:
    def solve(self, matrix):
        digits = {1,2,3,4,5,6,7,8,9}

        for row in matrix:
            if set(row) != digits:
                return False

        for c in range(len(matrix[0])):
            if {matrix[r][c] for r in range(len(matrix))} != digits:
                return False

        for box in range(9):
            r,c = 3*(box//3), 3*(box%3)

            if {matrix[r2][c2] for r2 in range(r,r+3) for c2 in range(c,c+3)} != digits:
                return False

        return True
