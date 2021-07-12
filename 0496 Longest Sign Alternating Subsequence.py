class Solution:
    def solve(self, nums):
        ans = [0,0]

        for num in nums:
            if num > 0:
                ans[0] = ans[1] + 1
            else:
                ans[1] = ans[0] + 1

        return max(ans)
