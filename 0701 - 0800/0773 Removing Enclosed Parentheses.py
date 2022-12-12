class Solution:
    def solve(self, s):
        pairs = []
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                pairs.append([stack.pop(),i])

        ans = 0

        while pairs and pairs[-1] == [ans,len(s)-1-ans]:
            ans += 1
            pairs.pop()


        return s[ans:-ans] if ans > 0 else s
