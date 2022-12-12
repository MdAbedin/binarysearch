class Solution:
    def solve(self, intervals):
        intervals.sort(key = lambda pair: [pair[0], -pair[1]])
        max_end = -inf
        ans = 0

        for a,b in intervals:
            if max_end >= b: ans += 1
            max_end = max(max_end, b)

        return ans
