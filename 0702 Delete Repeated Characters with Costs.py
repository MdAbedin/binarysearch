class Solution:
    def solve(self, s, nums):
        return sum(sum(streak_costs)-max(streak_costs) for streak_costs in map(lambda x: [nums[k] for k in list(x[1])], groupby(range(len(nums)), lambda j: s[j])))
