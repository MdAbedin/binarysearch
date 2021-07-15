class Solution:
    def solve(self, nums, k):
        rcounts = defaultdict(int,Counter(nums))

        for i in range(len(nums)):
            rcounts[nums[i]] -= 1
            for j in range(i):
                if rcounts[k-nums[i]-nums[j]] > 0: return True

        return False
