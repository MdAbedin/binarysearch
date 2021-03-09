class Solution:
    def solve(self, s, t):
        return all(x%2 == 0 for x in Counter(s+t).values())
