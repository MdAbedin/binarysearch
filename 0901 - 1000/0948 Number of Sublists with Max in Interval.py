class Solution:
    def solve(self, nums, lo, hi):
        start = -1
        end = -1
        ans = 0

        for i,num in enumerate(nums):
            if nums[i] > hi: start = i
            else:
                if nums[i] >= lo: end = i
                ans += max(0,end-start)

        return ans
