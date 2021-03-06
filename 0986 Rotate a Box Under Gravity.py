class Solution:
    def solve(self, matrix):
        matrix = [[matrix[r][c] for r in range(len(matrix)-1,-1,-1)] for c in range(len(matrix[0]))]

        for j in range(len(matrix[0])):
            lowest_empty = -1

            for i in range(len(matrix)-1,-1,-1):
                if matrix[i][j] == "#":
                    if lowest_empty != -1:
                        matrix[lowest_empty][j] = "#"
                        matrix[i][j] = "."
                        lowest_empty -= 1
                elif matrix[i][j] == ".":
                    lowest_empty = max(lowest_empty, i)
                else:
                    lowest_empty = -1

        return matrix
