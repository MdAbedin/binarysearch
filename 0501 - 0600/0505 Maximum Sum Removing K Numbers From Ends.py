class Solution:
    def solve(self, nums, k):
        total = sum(nums[:k])
        ans = total

        for i in range(k):
            total -= nums[k-i-1]
            total += nums[~i]
            ans = max(ans,total)

        return ans
