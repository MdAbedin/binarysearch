class Solution:
    def solve(self, s):
        a0 = 0
        b1 = s.count("1")
        ans = -inf

        for i in range(len(s)-1):
            if s[i] == "0":
                a0 += 1
            else:
                b1 -= 1

            ans = max(ans,a0+b1)

        return ans
