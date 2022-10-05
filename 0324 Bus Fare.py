class Solution:
    def solve(self, days):
        days.sort()
        costs = []

        for day in days:
            cost = inf
            
            i = bisect_right(costs,[day-1,inf])-1
            cost = min(cost, (costs[i][1] if i >= 0 else 0) + 2)

            i = bisect_right(costs,[day-7,inf])-1
            cost = min(cost, (costs[i][1] if i >= 0 else 0) + 7)
            
            i = bisect_right(costs,[day-30,inf])-1
            cost = min(cost, (costs[i][1] if i >= 0 else 0) + 25)

            costs.append([day,cost])

        return costs[-1][1]
