class Solution:
    def solve(self, matrix):
        pq = [[0, i] for i in range(len(matrix[0]))]

        for r in range(len(matrix)):
            new_pq = []

            for c in range(len(matrix[0])):
                if pq[0][1] == c:
                    top = heappop(pq)
                    heappush(new_pq, [pq[0][0]+matrix[r][c], c])
                    heappush(pq, top)
                else:
                    heappush(new_pq, [pq[0][0]+matrix[r][c], c])

            pq = new_pq

        return pq[0][0]
