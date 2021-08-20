class Solution:
    def solve(self, matrix):
        n = len(matrix)
        nums = set(range(1,n+1))
        row_choices = [nums - set(row) for row in matrix]
        col_choices = [nums - {row[c] for row in matrix} for c in range(n)]

        def helper(r,c):
            if r == n: return True
            if c == n: return helper(r+1,0)
            if matrix[r][c] != 0: return helper(r,c+1)

            for choice in row_choices[r] & col_choices[c]:
                matrix[r][c] = choice
                row_choices[r].remove(choice)
                col_choices[c].remove(choice)

                if helper(r,c+1): return True

                matrix[r][c] = 0
                row_choices[r].add(choice)
                col_choices[c].add(choice)

            return False

        helper(0,0)

        return all(set(row) == nums for row in matrix) and all({row[c] for row in matrix} == nums for c in range(n))
