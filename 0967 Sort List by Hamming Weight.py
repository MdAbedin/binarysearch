class Solution:
    def solve(self, nums):
        return sorted(nums, key=lambda x: [bin(x).count("1"), x])
