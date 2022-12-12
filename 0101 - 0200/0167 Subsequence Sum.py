class Solution:
    def solve(self, nums):
        sums = defaultdict(int)

        for i,num in enumerate(nums):
            sums[num-i] += num

        return max(sums.values())
