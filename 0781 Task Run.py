class Solution:
    def solve(self, tasks, k):
        if not tasks: return 0

        last_times = defaultdict(lambda: -inf)
        t = 0

        for task in tasks:
            t = max(t+1,last_times[task]+k+1)
            last_times[task] = t

        return t
