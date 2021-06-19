class Solution:
    def solve(self, nums):
        return (sum(x-1 for x in Counter(nums).values())+1)//2
