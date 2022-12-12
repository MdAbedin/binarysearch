class Solution:
    def solve(self, matrix):
        R,C = len(matrix),len(matrix[0])
        ID = 2

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 1:
                    dfs = [[r,c]]
                    matrix[r][c] = ID

                    while dfs:
                        r2,c2 = dfs.pop()

                        for r3,c3 in [[r2+1,c2],[r2-1,c2],[r2,c2+1],[r2,c2-1]]:
                            if r3 in range(R) and c3 in range(C) and matrix[r3][c3] == 1:
                                matrix[r3][c3] = ID
                                dfs.append([r3,c3])

                    ID += 1

        border_ids = set()

        for r in [0,R-1]:
            for c in range(C):
                if matrix[r][c] > 1:
                    border_ids.add(matrix[r][c])

        for c in [0,C-1]:
            for r in range(R):
                if matrix[r][c] > 1:
                    border_ids.add(matrix[r][c])

        return ID-2 - len(border_ids)
