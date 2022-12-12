class Solution:
    def solve(self, nums):
        dp = []

        for i in range(len(nums)):
            new = defaultdict(lambda: defaultdict(int, {1:1}))

            for j in range(i):
                diff = nums[i] - nums[j]

                for size in dp[j][diff]:
                    new[diff][size+1] += dp[j][diff][size]

            dp.append(new)

        return sum(d[diff][size] for d in dp for diff in d for size in d[diff] if size >= 3)
