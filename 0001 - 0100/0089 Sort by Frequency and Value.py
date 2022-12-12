class Solution:
    def solve(self, nums):
        freqs = Counter(nums)
        nums.sort(key=lambda x: [-freqs[x], -x])
        return nums
