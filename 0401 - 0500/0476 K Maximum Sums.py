class Solution:
    def solve(self, nums, k):
        nums = [0]+nums
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        sums = [[nums[i] - x for x in sorted(nums[:i])[:k]] for i in range(1,len(nums))]
        return sorted(sum(sums,[]))[-k:]
