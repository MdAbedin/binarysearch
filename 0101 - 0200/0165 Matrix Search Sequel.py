class Solution:
    def solve(self, matrix, target):
        dfs = [[0,0]]
        seen = {(0,0)}

        while dfs:
            r,c = dfs.pop()
            if matrix[r][c] == target: return True

            if r+1<len(matrix) and (r+1,c) not in seen:
                seen.add((r+1,c))
                dfs.append([r+1,c])
            if c+1<len(matrix[0]) and (r,c+1) not in seen:
                seen.add((r,c+1))
                dfs.append([r,c+1])

        return False
