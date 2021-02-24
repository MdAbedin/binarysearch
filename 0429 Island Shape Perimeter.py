class Solution:
    def solve(self, matrix):
        ans = 0

        for y in range(len(matrix)):
          for x in range(len(matrix[0])):
            if matrix[y][x] == 1:
              neighbors = 0

              for ny,nx in [[y+1,x], [y-1,x], [y,x+1], [y,x-1]]:
                if 0<=ny<len(matrix) and 0<=nx<len(matrix[0]) and matrix[ny][nx] == 1: neighbors += 1

              ans += 4-neighbors

        return ans
