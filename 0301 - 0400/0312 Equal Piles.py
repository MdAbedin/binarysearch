class Solution:
    def solve(self, nums):
        sorted_nums = sorted(list(set(nums)))
        locs = {sorted_nums[i]:i for i in range(len(sorted_nums))}

        return sum(locs[num] for num in nums)
