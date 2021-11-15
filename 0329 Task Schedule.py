class Solution:
    def solve(self, nums, k):
        counts = Counter(nums)
        max_c = max(counts.values())

        return max(len(nums), (max_c-1)*(k+1) + sum(c == max_c for c in counts.values()))
