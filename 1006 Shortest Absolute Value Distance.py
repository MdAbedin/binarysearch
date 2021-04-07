class Solution:
    def solve(self, matrix):
        bests = [[inf]*len(matrix[0]) for i in range(len(matrix))]
        pq = [[0,[0,0]]]

        while pq:
            cost,loc = heappop(pq)
            cr,cc = loc

            if (cr,cc) == (len(matrix)-1,len(matrix[0])-1): return cost

            if cost > bests[cr][cc]: continue

            for nr,nc in [[cr+1,cc],[cr-1,cc],[cr,cc+1],[cr,cc-1]]:
                if 0<=nr<len(matrix) and 0<=nc<len(matrix[0]) and cost + abs(matrix[nr][nc]-matrix[cr][cc]) < bests[nr][nc]:
                    bests[nr][nc] = cost + abs(matrix[nr][nc]-matrix[cr][cc])
                    heappush(pq,[cost + abs(matrix[nr][nc]-matrix[cr][cc]), [nr,nc]])
