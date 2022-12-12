class Solution:
    def solve(self, nums):
        nums.sort()
        ks = copy.copy(nums)
        ans = 0

        for j in range(len(nums)):
            ks.remove(nums[j])

            for i in range(j):
                ans += bisect_left(ks, nums[i] + nums[j])

        return ans
