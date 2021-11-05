class Solution:
    def solve(self, nums, k):
        if k == 0: return 0

        sublist_max = 0
        cur = 0

        for num in nums:
            cur += num
            cur = max(cur,0)
            sublist_max = max(sublist_max, cur)

        if k == 1: return sublist_max

        suffix_sums = [0]+list(accumulate(nums[::-1]))
        prefix_sums = [0]+list(accumulate(nums))

        return max(sublist_max, max(suffix_sums) + max(0,(k-2)*sum(nums)) + max(prefix_sums))
