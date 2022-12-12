class Solution:
    def solve(self, s, t):
        return min(sum(t[j] != s[i+j] for j in range(len(t))) for i in range(len(s)-len(t)+1))
