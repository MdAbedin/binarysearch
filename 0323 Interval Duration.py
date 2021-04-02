class Solution:
    def solve(self, intervals):
        intervals.sort()
        merged = []

        for a,b in intervals:
            if not merged or a > merged[-1][1]: merged.append([a,b])
            else: merged[-1][1] = max(merged[-1][1],b)

        return sum(b-a+1 for a,b in merged)
