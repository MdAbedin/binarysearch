class Solution:
    def solve(self, nums):
        cur = 0
        switches = 0

        for num in nums:
            if num != cur:
                cur = 1-cur
                switches += 1

        return switches
