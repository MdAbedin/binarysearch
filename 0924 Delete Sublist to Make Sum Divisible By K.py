class Solution:
    def solve(self, nums, k):
        total = sum(nums)

        if total%k == 0: return 0
        
        psums = list(accumulate(nums))
        latests = {0:-1}
        ans = inf

        for i,psum in enumerate(psums):
            if (psum%k - total%k)%k in latests: ans = min(ans, i-latests[(psum%k - total%k)%k])
            latests[psum%k] = i

        return -1 if ans >= len(nums) else ans
