class Solution:
    def solve(self, s):
        MOD = 10**9+7
        locs = [i for i in range(len(s)) if s[i] == "1"]
        total = sum(map(int, s))

        if total == 0:
            return (((len(s)-1)*(len(s)-2))//2)%MOD
        elif total%3 == 0:
            return ((locs[total//3]-locs[total//3-1])*(locs[-total//3]-locs[-total//3-1]))%MOD
        else:
            return 0
