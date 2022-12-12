class Solution:
    def solve(self, matrix):
        row_maxes = [max(row) for row in matrix]
        col_maxes = [max([row[i] for row in matrix]) for i in range(len(matrix[0]))]

        return [[min(row_maxes[y], col_maxes[x]) for x in range(len(matrix[0]))] for y in range(len(matrix))]
