class Solution:
    def solve(self, s):
        if not s:
            return 0
            
        left_streaks = [0]

        for i in range(len(s)):
            left_streaks.append(left_streaks[-1]+1 if s[i] == '1' else 0)

        right_streaks = [0]

        for i in range(len(s)-1,-1,-1):
            right_streaks.append(right_streaks[-1]+1 if s[i] == '1' else 0)

        right_streaks.reverse()

        return max(left_streaks[i]+right_streaks[i+1]+1 for i in range(len(s)))
