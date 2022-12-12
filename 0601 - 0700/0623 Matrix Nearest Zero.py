class Solution:
    def solve(self, matrix):
        zeros = []
        pq = []
        bests = [[inf]*len(matrix[0]) for row in matrix]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeros.append((r,c))
                    heappush(pq, [0, [r,c]])
                    bests[r][c] = 0

        while pq:
            d, (r,c) = heappop(pq)

            for nr,nc in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                if 0<=nr<len(matrix) and 0<=nc<len(matrix[0]) and d+1 < bests[nr][nc]:
                    bests[nr][nc] = d+1
                    heappush(pq,[d+1,[nr,nc]])

        return bests
