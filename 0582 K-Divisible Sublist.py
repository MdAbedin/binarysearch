class Solution:
    def solve(self, nums, k):
        mods = set()
        last = 0
        psum = 0

        for num in nums:
            psum += num
            if psum%k in mods: return True
            mods.add(last)
            last = psum%k

        return False
