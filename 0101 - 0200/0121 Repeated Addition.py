class Solution:
    def solve(self, n):
        while n >=10:
          n = sum([int(x) for x in str(n)])
        return n
