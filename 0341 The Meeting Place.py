class Solution:
    def solve(self, matrix):
        dists_and_counts = [[[0,0] for col in row] for row in matrix]
        ppl_count = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 2:
                    ppl_count += 1
                    bfs = deque([[r,c,0]])
                    seen = {(r,c)}

                    while bfs:
                        cr,cc,d = bfs.popleft()

                        dists_and_counts[cr][cc][0] += d
                        dists_and_counts[cr][cc][1] += 1

                        for nr,nc in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:
                            if 0<=nr<len(matrix) and 0<=nc<len(matrix[0]) and matrix[nr][nc] != 1 and (nr,nc) not in seen:
                                seen.add((nr,nc))
                                bfs.append([nr,nc,d+1])

        return min(cell[0] for row in dists_and_counts for cell in row if cell[1] == ppl_count)
