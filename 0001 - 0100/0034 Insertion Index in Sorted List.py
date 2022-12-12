class Solution:
    def solve(self, nums, target):
        return bisect_right(nums, target)
