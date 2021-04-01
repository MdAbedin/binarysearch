class Solution:
    def solve(self, nums):
        nums.sort()
        ans = 0
        mx = -inf

        for i in range(len(nums)-1,-1,-1):
            if nums[i]+len(nums) >= mx: ans += 1
            mx = max(mx, nums[i]+(len(nums)-i))

        return ans
