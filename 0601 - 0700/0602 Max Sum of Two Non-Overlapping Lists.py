class Solution:
    def solve(self, nums, a, b):
        dp_a,dp_b = [-inf],[-inf]
        cur_a,cur_b = 0,0
        ans = -inf

        for i in range(len(nums)):
            cur_a += nums[i]
            cur_b += nums[i]

            if i-a >= 0: cur_a -= nums[i-a]
            if i-b >= 0: cur_b -= nums[i-b]

            dp_a.append(-inf if i < a-1 else max(dp_a[-1], cur_a))
            dp_b.append(-inf if i < b-1 else max(dp_b[-1], cur_b))

            if i >= a+b-1: ans = max(ans, cur_a + dp_b[-a-1], cur_b + dp_a[-b-1])

        return ans
