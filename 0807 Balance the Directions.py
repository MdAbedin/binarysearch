class Solution:
    def solve(self, s):
        return min((min(locs[char][i]-(min((locs[c2][x] if (x := bisect_right(locs[c2], locs[char][i])-1-(len(locs[c2])-len(s)//4-1)) >= 0 else -inf for c2 in "NEWS" if len(locs[c2]) > len(s)//4),default=-inf))+1 for i in range(len(locs[char]))) for char in "NEWS" if len((locs := {c:[i for i in range(len(s)) if s[i] == c] for c in "NEWS"})[char]) > len(s)//4), default=0)
