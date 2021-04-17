class Solution:
    def solve(self, s):
        l = -1
        ans = []
        for c in s:
            if c == "(":
                l += 1
            elif c == ")":
                l -= 1
            else:
                while l >= len(ans):
                    ans.append(0)
                ans[l] += 1

            while l >= len(ans):
                    ans.append(0)

        return ans
