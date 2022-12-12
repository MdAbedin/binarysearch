class Solution:
    def solve(self, nums, k):
        ans = -1
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            if total <= k: ans = i

        return ans
