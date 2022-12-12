class Solution:
    def solve(self, nums, k):
        nums.sort()
        return sum(2**(j-i-1) for i in range(len(nums)) if (j := bisect_right(nums,k-nums[i])) > i)
