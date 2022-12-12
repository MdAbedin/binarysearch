class Solution:
    def solve(self, nums):
        if not nums: return 0

        return sum((x**2 + x)//2 for x in Counter(nums).values())
