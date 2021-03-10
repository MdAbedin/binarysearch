class Solution:
    def solve(self, s, i, j):
        s2 = ""
        while len(s2) <= j-i+1: s2 += s
        s2 += s
        return s2[i%len(s):i%len(s)+(j-i)]
