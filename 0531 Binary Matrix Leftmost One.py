class Solution:
    def solve(self, matrix):
        return min((bisect_left(row,1) for row in matrix if row and bisect_left(row,1) < len(row) and row[bisect_left(row,1)] == 1), default=-1)
