class Solution:
    def solve(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2

        if n%3 == 0:
            return 3**(n//3)
        elif n%3 == 1:
            return 4*(3**(n//3-1))
        else:
            return 2*(3**(n//3))
