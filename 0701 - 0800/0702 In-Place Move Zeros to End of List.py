class Solution:
    def solve(self, nums):
        return [num for num in nums if num != 0] + [0]*nums.count(0)
