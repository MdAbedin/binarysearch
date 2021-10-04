class Solution:
    def solve(self, intervals):
        intervals.sort(key = lambda x: x[1])
        keep = 0
        end = -1

        for a,b in intervals:
            if a >= end:
                end = b
                keep += 1

        return len(intervals) - keep
