class Solution:
    def solve(self, s):
        c = 0
        last_char = ""
        ans = 0

        for i in range(len(s)):
            if last_char == s[i]:
                c += 1
            else:
                c = 1
                last_char = s[i]
            ans += c

        return ans
