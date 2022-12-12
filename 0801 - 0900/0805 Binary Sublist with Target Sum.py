class Solution:
    def solve(self, nums, target):
        nums = list(accumulate(nums))
        counts = defaultdict(int, {0:1})
        ans = 0

        for i in range(len(nums)):
            ans += counts[nums[i]-target]
            counts[nums[i]] += 1

        return ans
