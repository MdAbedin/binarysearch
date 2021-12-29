class Solution:
    def solve(self, matrix):
        if not matrix or not matrix[0]: return 0
        
        R,C = len(matrix), len(matrix[0])
        counts = defaultdict(int)

        def search(r,c,color):
            if r not in range(R) or c not in range(C): return
            if matrix[r][c] != color: return

            matrix[r][c] = -1

            search(r-1,c,color)
            search(r+1,c,color)
            search(r,c-1,color)
            search(r,c+1,color)

        for r in range(R):
            for c in range(C):
                if matrix[r][c] != -1:
                    color = matrix[r][c]
                    counts[color] += 1
                    search(r,c,color)

        return sum(counts.values()) - max(counts.values())
