class Solution:
    def solve(self, nums, k):
        counts = Counter(nums)

        for num in counts:
            if k-num == num:
                if counts[num] > 1: return True
            else:
                if k-num in counts: return True

        return False
