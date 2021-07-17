class Solution:
    def solve(self, nums):
        nums.sort()
        ans = []
        i = 0

        while i < len(nums):
            if bisect_right(nums,nums[i]) - bisect_left(nums,nums[i]) > len(nums)//3: ans.append(nums[i])
            i = bisect_right(nums,nums[i])

        return ans
