class Solution:
    def solve(self, nums):
        if not nums: return 0
        locs = defaultdict(lambda: inf, {0:-1})
        psum = 0
        ans = -inf

        for i,num in enumerate(nums):
            psum += -1 if num == 0 else 1
            locs[psum] = min(locs[psum], i)
            ans = max(ans, i - locs[psum])

        return len(nums)-ans
