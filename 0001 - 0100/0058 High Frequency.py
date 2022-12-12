class Solution:
    def solve(self, nums):
        if not nums: return 0
        return Counter(nums).most_common(1)[0][1]
