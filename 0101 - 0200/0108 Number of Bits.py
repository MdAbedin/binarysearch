class Solution:
    def solve(self, n):
        return bin(n)[2:].count("1")
