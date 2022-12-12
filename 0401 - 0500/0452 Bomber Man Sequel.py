class Solution:
    def solve(self, matrix):
        R,C = len(matrix),len(matrix[0])

        runs = [[[1,1,1,1] if matrix[r][c] == 2 else [0,0,0,0] for c in range(C)] for r in range(R)]

        for r in range(R):
            for c in range(C):
                if matrix[r][c] in [0,2]:
                    if r-1 >= 0: runs[r][c][0] += runs[r-1][c][0]
                    if c-1 >= 0: runs[r][c][1] += runs[r][c-1][1]

        for r in reversed(range(R)):
            for c in reversed(range(C)):
                if matrix[r][c] in [0,2]:
                    if r+1 < R: runs[r][c][2] += runs[r+1][c][2]
                    if c+1 < C: runs[r][c][3] += runs[r][c+1][3]

        return max((sum(runs[r][c]) for r in range(R) for c in range(C) if matrix[r][c] == 0),default = 0)
