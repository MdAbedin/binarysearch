class Solution:
    def solve(self, matrix):
        N = len(matrix)

        if not all(row.count(1) == 1 for row in matrix):
            return False

        if not all(col.count(1) == 1 for col in zip(*matrix)):
            return False

        if any([[matrix[y-x][x] for x in range(N) if 0<=y-x<N].count(1) > 1 for y in range(2*N-1)]):
            return False
        
        if any([[matrix[y-x][N-1-x] for x in range(N) if 0<=y-x<N].count(1) > 1 for y in range(2*N-1)]):
            return False

        return True
