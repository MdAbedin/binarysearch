class Solution:
    def solve(self, trips, capacity):
        deltas = defaultdict(int)
        endpoints = set()

        for start,end,num in trips:
            deltas[start] += num
            deltas[end] -= num
            endpoints.add(start)
            endpoints.add(end)

        sorted_endpoints = sorted(list(endpoints))
        used_capacity = 0

        for endpoint in sorted_endpoints:
            used_capacity += deltas[endpoint]
            if used_capacity > capacity: return False

        return True
