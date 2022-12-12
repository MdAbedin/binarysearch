class Solution:
    def solve(self, nums):
        if len(nums) <= 1:return len(nums)

        ans = 2
        i,j = 0,1
        streak = 2
        d = abs(nums[1]-nums[0])

        while j <= len(nums)-2:
            if abs(nums[j+1]-nums[j]) == d:
                j += 1
                streak += 1
            else:
                d = abs(nums[j+1]-nums[j])
                i = j
                j = j+1
                streak = 2

            ans = max(ans, streak)

        return ans
