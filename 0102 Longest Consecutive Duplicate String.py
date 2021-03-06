class Solution:
    def solve(self, s):
        last_char = ""
        cur_streak_length = 0
        best_ans = 0

        for i in range(len(s)):
          cur_char = s[i]

          if cur_char == last_char:
            cur_streak_length += 1
          else:
            cur_streak_length = 1
            last_char = cur_char

          best_ans = max(best_ans, cur_streak_length)

        return best_ans
