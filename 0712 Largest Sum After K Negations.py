class Solution:
    def solve(self, nums, k):
        nums.sort()

        for i in range(len(nums)):
            if nums[i] >= 0: break
            nums[i] *= -1
            k -= 1
            if k == 0: break

        return sum(nums) if k%2 == 0 else sum(nums)-2*min(nums)
