class Solution:
    def solve(self, matrix, k):
        for y in range(len(matrix)):
          for x in range(len(matrix[0])):
            if y-1>=0: matrix[y][x] += matrix[y-1][x]
            if x-1>=0: matrix[y][x] += matrix[y][x-1]
            if y-1>=0 and x-1>=0: matrix[y][x] -= matrix[y-1][x-1]
            
        return [[matrix[min(len(matrix)-1, y+k)][min(len(matrix[0])-1, x+k)] - (matrix[y-k-1][min(len(matrix[0])-1,x+k)] if y-k-1>=0 else 0) - (matrix[min(len(matrix)-1,y+k)][x-k-1] if x-k-1>=0 else 0) + (matrix[y-k-1][x-k-1] if y-k-1>=0 and x-k-1>=0 else 0) for x in range(len(matrix[0]))] for y in range(len(matrix))]
