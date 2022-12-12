class Solution:
    def solve(self, nums):
        return [int(char) for char in str(int("".join(str(d) for d in nums))+1)]
