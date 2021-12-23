class Solution:
    def solve(self, nums):
        dp = [1,2]
        ans = 0

        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp.append(dp[-1]+1)
                ans += dp[-1] - 2
            else:
                dp.append(2)

        return ans
