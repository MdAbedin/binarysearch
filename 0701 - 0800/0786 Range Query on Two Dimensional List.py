class RangeSumMatrix:
    def __init__(self, matrix):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] += matrix[r-1][c] if r-1 >= 0 else 0
                matrix[r][c] += matrix[r][c-1] if c-1 >= 0 else 0
                matrix[r][c] -= matrix[r-1][c-1] if r-1 >= 0 and c-1 >= 0 else 0

        self.matrix = matrix

    def total(self, r0,c0,r1,c1):
        ans = self.matrix[r1][c1]
        ans -= self.matrix[r0-1][c1] if r0-1 >= 0 else 0
        ans -= self.matrix[r1][c0-1] if c0-1 >= 0 else 0
        ans += self.matrix[r0-1][c0-1] if r0-1 >= 0 and c0-1 >= 0 else 0

        return ans
