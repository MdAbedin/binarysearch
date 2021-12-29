class Solution:
    def solve(self, matrix):
        if not matrix or not matrix[0]: return matrix

        R,C = len(matrix),len(matrix[0])
        water_locs = []

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    water_locs.append([r,c])
                    
        return [[0 if matrix[r][c] == 0 else min(abs(r-r2) + abs(c-c2) for r2,c2 in water_locs)  for c in range(C)] for r in range(R)]
