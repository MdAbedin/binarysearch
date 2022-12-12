class Solution:
    def solve(self, matrix):
        if matrix[0][0] == 1: return -1
        R,C = len(matrix),len(matrix[0])
        bfs = deque([[0,0]])
        dists = {(0,0): 1}

        while bfs:
            r,c = bfs.popleft()
            if (r,c) == (R-1,C-1): return dists[r,c]
            
            for nr,nc in [[r-1,c],[r+1,c],[r,c-1],[r,c+1]]:
                if 0<=nr<R and 0<=nc<C and (nr,nc) not in dists and matrix[nr][nc] == 0:
                    dists[nr,nc] = dists[r,c] + 1
                    bfs.append((nr,nc))

        return -1
