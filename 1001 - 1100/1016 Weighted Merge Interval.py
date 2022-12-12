class Solution:
    def solve(self, intervals):
        endpoints = sorted(list(set({endpoint for interval in intervals for endpoint in interval[:-1]})))
        weights = [0]*(len(endpoints)+1)
        locs = {endpoints[i]:i for i in range(len(endpoints))}
        starts,ends = defaultdict(int), defaultdict(int)

        for a,b,w in intervals:
            starts[locs[a]] += w
            weights[locs[a]] += w
            ends[locs[b]] += w
            weights[locs[b]+1] -= w

        for i in range(len(weights)):
            weights[i] += weights[i-1]

        max_weight = max(weights)
        ans = [[-inf,-inf]]

        for i in range(len(weights)-1):
            if weights[i] != max_weight: continue

            if i==0 or (ends[i-1] > 0 and ans[-1][1] != endpoints[i]-1) or weights[i-1] != max_weight: ans.append([endpoints[i],endpoints[i]])
            else: ans[-1][1] = endpoints[i]

        return ans[1:]
