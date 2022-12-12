class Solution:
    def solve(self, nums, diff):
        maxes = defaultdict(int)

        for num in nums:
            maxes[num] = max(maxes[num], 1 + maxes[num-diff])

        return max(maxes.values())
