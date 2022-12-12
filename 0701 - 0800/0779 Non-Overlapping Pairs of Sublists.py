class Solution:
    def solve(self, nums, k):
        MOD = 10**9+7
        streak, sublists_before = 0,0
        prev_streak_ans = 0
        ans = 0

        for num in nums:
            if num >= k:
                streak += 1

                cur_streak_ans = prev_streak_ans + (streak-1)*streak//2
                cur_streak_ans %= MOD
                prev_streak_ans = cur_streak_ans
                
                ans += cur_streak_ans + streak * sublists_before
                ans %= MOD
            else:
                sublists_before += streak*(streak+1)//2
                sublists_before %= MOD
                streak = 0
                prev_streak_ans = 0

        return ans
