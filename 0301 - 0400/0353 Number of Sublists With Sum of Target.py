class Solution:
    def solve(self, nums, target):
        prefix_sums = nums
        for i in range(1,len(prefix_sums)):
            prefix_sums[i] += prefix_sums[i-1]

        ans = 0
        counts = defaultdict(int)
        counts[0] = 1
        
        for end in range(len(prefix_sums)):
            ans += counts[prefix_sums[end] - target]
            counts[prefix_sums[end]] += 1

        return ans
