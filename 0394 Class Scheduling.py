class Solution:
    def solve(self, times):
        ends = [-1]+sorted(list({time[1] for time in times}))
        locs = {ends[i]:i for i in range(len(ends))}
        dp = [0]*len(ends)
        times.sort(key=lambda x: x[1])
        for s,e in times:
            dp[locs[e]] = max(dp[locs[e]], dp[bisect_left(ends,s)-1]+1, dp[locs[e]-1])
        return dp[-1]
