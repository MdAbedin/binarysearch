class Solution:
    def solve(self, matrix):
        total = sum(sum(row) for row in matrix)
        escapable = 0
        seen = set()

        for r in range(len(matrix)):
            for c in [0,len(matrix[0])-1]:
                if (r,c) in seen or matrix[r][c] != 1:
                    continue

                seen.add((r,c))
                dfs = [[r,c]]
                
                while dfs:
                    cr,cc = dfs.pop()
                    escapable += 1

                    for nr,nc in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:
                        if 0<=nr<len(matrix) and 0<=nc<len(matrix[0]) and (nr,nc) not in seen and matrix[nr][nc] == 1:
                            dfs.append([nr,nc])
                            seen.add((nr,nc))

        for r in [0,len(matrix)-1]:
            for c in range(len(matrix[0])):
                if (r,c) in seen or matrix[r][c] != 1:
                    continue

                seen.add((r,c))
                dfs = [[r,c]]
                
                while dfs:
                    cr,cc = dfs.pop()
                    escapable += 1

                    for nr,nc in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:
                        if 0<=nr<len(matrix) and 0<=nc<len(matrix[0]) and (nr,nc) not in seen and matrix[nr][nc] == 1:
                            dfs.append([nr,nc])
                            seen.add((nr,nc))

        return total - escapable
