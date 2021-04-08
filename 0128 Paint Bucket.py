class Solution:
    def solve(self, matrix, r, c, target):
        dfs = [[r,c]]
        original_color = matrix[r][c]
        seen = {(r,c)}

        while dfs:
            cr,cc = dfs.pop()
            matrix[cr][cc] = target

            for nr,nc in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:
                if 0<=nr<len(matrix) and 0<=nc<len(matrix[0]) and (nr,nc) not in seen and matrix[nr][nc]==original_color:
                    dfs.append([nr,nc])
                    seen.add((nr,nc))

        return matrix
