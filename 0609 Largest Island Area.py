class Solution:
    def solve(self, matrix):
        ans = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] != 1:
                    continue

                matrix[r][c] = 2
                dfs = [[r,c]]
                size = 0

                while dfs:
                    cr,cc = dfs.pop()
                    size += 1

                    for nr,nc in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:
                        if 0<=nr<len(matrix) and 0<=nc<len(matrix[0]) and matrix[nr][nc] == 1:
                            matrix[nr][nc] = 2
                            dfs.append([nr,nc])

                ans = max(ans, size)

        return ans
