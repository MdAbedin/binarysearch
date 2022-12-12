class Solution:
    def solve(self, intervals):
        if not intervals: return 0

        intervals.sort(key=lambda x: x[1])
        min_sizes = [[-inf,inf]]
        for a,b in intervals:
            min_sizes.append([b,min(min_sizes[-1][1], b-a+1)])

        intervals.sort()
        ans = inf
        i = 0

        for a,b in intervals:
            while i < len(min_sizes)-1 and min_sizes[i+1][0] < a:
                i += 1
            ans = min(ans, b-a+1+min_sizes[i][1])

        return 0 if ans == inf else ans
