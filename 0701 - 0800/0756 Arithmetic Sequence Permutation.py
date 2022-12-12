class Solution:
    def solve(self, nums):
        return len(set(nxt-cur for cur,nxt in zip(sorted(nums), sorted(nums)[1:]))) == 1
