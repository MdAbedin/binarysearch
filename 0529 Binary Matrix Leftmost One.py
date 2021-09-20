class Solution:
    def solve(self, matrix):
        return min(bisect_left(row,1) for row in matrix) if 1 in sum((row for row in matrix), []) else -1
