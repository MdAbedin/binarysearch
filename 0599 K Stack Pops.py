class Solution:
    def solve(self, stacks, k):
        if not stacks or k == 0: return 0

        for row in stacks: row.reverse()

        dp = [0]+list(accumulate(stacks[0]))
        while len(dp) < k+1: dp.append(-inf)

        for stack in stacks[1:]:
            dp2 = copy.copy(dp)

            for used in range(k+1):
                cur_sum = 0

                for cur_used in range(min(len(stack),used)+1):
                    dp2[used] = max(dp2[used], cur_sum + dp[used - cur_used])
                    if cur_used < len(stack): cur_sum += stack[cur_used]

            dp = dp2

        return dp[k]
