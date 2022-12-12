class Solution:
    def solve(self, nums, target):
        nums.sort()
        ans = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ans += max(0, bisect_left(nums, target-nums[i]-nums[j]) - j - 1)

        return ans
