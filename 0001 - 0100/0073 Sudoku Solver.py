class Solution:
    def solve(self, matrix):
        rchoices = [set(range(1,10)) for i in range(9)]
        cchoices = [set(range(1,10)) for i in range(9)]
        bchoices = [set(range(1,10)) for i in range(9)]

        for r in range(9):
            for c in range(9):
                b = (r//3) * 3 + c//3
                rchoices[r].discard(matrix[r][c])
                cchoices[c].discard(matrix[r][c])
                bchoices[b].discard(matrix[r][c])

        def helper(r,c):
            if c == 9: return helper(r+1,0)
            if r == 9: return True
            if matrix[r][c] != 0: return helper(r,c+1)

            b = (r//3) * 3 + c//3

            for choice in rchoices[r] & cchoices[c] & bchoices[b]:
                matrix[r][c] = choice
                rchoices[r].remove(choice)
                cchoices[c].remove(choice)
                bchoices[b].remove(choice)

                if helper(r,c+1): return True

                matrix[r][c] = 0
                rchoices[r].add(choice)
                cchoices[c].add(choice)
                bchoices[b].add(choice)

            return False

        helper(0,0)
        return matrix
