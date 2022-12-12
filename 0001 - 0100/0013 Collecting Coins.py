class Solution:
    def solve(self, matrix):
        for y in range(len(matrix)):
          for x in range(len(matrix[0])):
            if y-1 >= 0 and x-1 >= 0:
              matrix[y][x] += max(matrix[y-1][x], matrix[y][x-1])
            elif y-1 >= 0:
              matrix[y][x] += matrix[y-1][x]
            elif x-1 >= 0:
              matrix[y][x] += matrix[y][x-1]

        return matrix[-1][-1]
