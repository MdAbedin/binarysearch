class Solution:
    def solve(self, s, t):
        return all(x<=y for x,y in zip(sorted(list(s)),sorted(list(t)))) or all(y<=x for x,y in zip(sorted(list(s)),sorted(list(t))))
