class Solution:
    def solve(self, s):
        s = [char for char in s if char.islower()]
        return s == s[::-1]
