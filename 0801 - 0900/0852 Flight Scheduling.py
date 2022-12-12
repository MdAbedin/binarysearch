class Solution:
    def solve(self, costs):
        costs.sort(key = lambda pair: pair[1]-pair[0], reverse = True)
        return sum(costs[i][i // (len(costs)//2)] for i in range(len(costs)))
