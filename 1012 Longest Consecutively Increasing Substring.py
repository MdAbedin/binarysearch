class Solution:
    def solve(self, s):
        s += chr(ord('a')-1)
        ans = 0
        last_char_i = -1
        streak = 0
        streaks = []

        for i in range(len(s)-1):
            if s[i] == "?":
                if streak < 26: streak += 1
            else:
                if s[i-1] == "?":
                    if (i-last_char_i-1) >= ord(s[i])-ord('a') or (streaks[last_char_i] > 0 and s[last_char_i] < s[i] and ord(s[last_char_i])+(i-last_char_i-1) >= ord(s[i])-1): streak = ord(s[i])-ord('a')+1
                    else: streak = 0
                else:
                    if s[i] == "a": streak = 1
                    elif streak > 0 and ord(s[i]) == ord(s[i-1])+1: streak += 1
                    else: streak = 0

                last_char_i = i
            
            streaks.append(streak)
            ans = max(ans,streak)

        return ans
