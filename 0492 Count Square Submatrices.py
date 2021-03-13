class Solution:
    def solve(self, matrix):
        ans = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 1:
                    v,h,s = 0,0,0

                    if r-1>=0:
                        v = matrix[r-1][c][0]
                    if c-1>=0:
                        h = matrix[r][c-1][1]
                    if r-1>=0 and c-1>=0:
                        s = matrix[r-1][c-1][2]

                    matrix[r][c] = [v+1,h+1,min(v,h,s)+1]
                    ans += matrix[r][c][-1]
                else:
                    matrix[r][c] = [0,0,0]

        return ans
