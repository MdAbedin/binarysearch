class Solution:
    def solve(self, nums):
        if len(nums) <= 1:
            return len(nums)

        sign = lambda x: (x>0)-(x<0)
        d = sign(nums[1]-nums[0])
        streak = 1 if d == 0 else 2
        ans = streak

        for i in range(1,len(nums)-1):
            if nums[i+1]-nums[i] == 0:
                streak = 1
            elif d == 0 or sign(nums[i+1]-nums[i]) == -d:
                streak += 1
            else:
                streak = 2

            d = sign(nums[i+1]-nums[i])
            ans = max(ans, streak)

        return ans
