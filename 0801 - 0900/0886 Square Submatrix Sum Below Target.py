class Solution:
    def solve(self, matrix, target):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r-1 >= 0: matrix[r][c] += matrix[r-1][c]
                if c-1 >= 0: matrix[r][c] += matrix[r][c-1]
                if r-1 >= 0 and c-1 >= 0: matrix[r][c] -= matrix[r-1][c-1]

        l,r = 0,min(len(matrix),len(matrix[0]))
        ans = 0

        def works(x):
            return any(matrix[r][c]-(matrix[r-x][c] if r-x>=0 else 0)-(matrix[r][c-x] if c-x>=0 else 0)+(matrix[r-x][c-x] if r-x>=0 and c-x>=0 else 0) <= target for r in range(x-1,len(matrix)) for c in range(x-1,len(matrix[0])))
        
        while l<=r:
            m = (l+r)//2

            if works(m):
                ans = m
                l = m+1
            else:
                r = m-1

        return ans**2
