class Solution:
    def solve(self, nums, target):
        counts = Counter(nums)
        return sum(min(counts[x], counts.get(target-x,0))//(2 if x == target-x else 1)*(2 if x == target-x else 1) for x in counts)//2
