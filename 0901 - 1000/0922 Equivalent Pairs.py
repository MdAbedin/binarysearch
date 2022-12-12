class Solution:
    def solve(self, nums):
        ans = 0
        counts = defaultdict(int)

        for num in nums:
            ans += counts[num]
            counts[num] += 1

        return ans
