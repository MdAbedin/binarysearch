class Solution:
    def solve(self, nums):
        return bisect_left(list(accumulate(sorted(Counter(nums).values(),reverse=True))), len(nums)/2)+1
