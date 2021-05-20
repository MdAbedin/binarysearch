class Solution:
    def solve(self, s):
        if not s:
            return 0

        Bs_to_left = [0]

        for i in range(len(s)):
            last = Bs_to_left[-1]
            Bs_to_left.append(last + (1 if s[i] == "B" else 0))
            
        As_to_right = [0]

        for i in range(len(s)-1,-1,-1):
            last = As_to_right[-1]
            As_to_right.append(last + (1 if s[i] == "A" else 0))

        As_to_right.reverse()

        ans = inf

        for i in range(len(s)+1):
            ans = min(ans, Bs_to_left[i] + As_to_right[i])

        return ans
