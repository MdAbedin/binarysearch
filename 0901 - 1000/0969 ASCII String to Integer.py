class Solution:
    def solve(self, s):
        s = "".join([c if c.isdigit() else " " for c in s])
        return sum(int(x) for x in s.split())
