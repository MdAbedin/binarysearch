class Solution:
    def solve(self, nums):
        ans = -inf
        cur_ans = 0

        for i in range(len(nums)):
            cur_ans = max(0,cur_ans)
            cur_ans += nums[i]
            ans = max(ans,cur_ans)

        return ans
