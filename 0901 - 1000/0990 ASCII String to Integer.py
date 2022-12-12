class Solution:
    def solve(self, s):
        return sum(int(x) for x in "".join([c if c.isdigit() else " " for c in s]).split())
